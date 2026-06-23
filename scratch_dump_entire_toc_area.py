import zipfile
import xml.etree.ElementTree as ET

def dump_toc_area(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
        'xlink': 'http://www.w3.org/1999/xlink',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        
        # Traverse elements sequentially in office:text
        body = root.find('.//office:text', namespaces)
        if body is not None:
            children = list(body)
            for idx, child in enumerate(children):
                if child.tag == f"{{{namespaces['text']}}}table-of-content":
                    print(f"\nFound TOC at index {idx}")
                    toc_xml = ET.tostring(child, encoding='utf-8').decode('utf-8')
                    print("TOC XML:")
                    print(toc_xml[:2000]) # First 2000 chars of TOC XML
                    print("...")
                    print(toc_xml[-1000:]) # Last 1000 chars of TOC XML

if __name__ == '__main__':
    dump_toc_area(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
