import zipfile
import xml.etree.ElementTree as ET

def extract_toc_xml(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        toc = root.find('.//text:table-of-content', namespaces)
        if toc is not None:
            # Re-register namespaces for clean serialization
            ET.register_namespace('text', namespaces['text'])
            toc_xml = ET.tostring(toc, encoding='utf-8').decode('utf-8')
            with open("scratch_toc_node.xml", "w", encoding="utf-8") as f:
                f.write(toc_xml)
            print("Successfully extracted TOC to scratch_toc_node.xml")
        else:
            print("TOC not found!")

if __name__ == '__main__':
    extract_toc_xml("DP-XMC-5049-000-V1-01-SRS-0V03.odt")
