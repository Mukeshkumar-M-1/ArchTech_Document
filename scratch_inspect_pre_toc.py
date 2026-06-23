import zipfile
import xml.etree.ElementTree as ET

def check_pre_toc(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
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
                    print(f"Found TOC at index {idx} in body")
                    # Print 5 elements before TOC
                    for i in range(max(0, idx-5), idx):
                        prev = children[i]
                        print(f"  Preceding {i-idx}: Element={prev.tag}, Attributes={prev.attrib}")
                        text_val = "".join(prev.itertext()).strip()
                        if text_val:
                            print(f"    Text: {text_val}")

if __name__ == '__main__':
    check_pre_toc("DP-XMC-5049-000-V1-01-SRS-0V03.odt")
