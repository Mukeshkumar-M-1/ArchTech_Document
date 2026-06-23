import zipfile
import xml.etree.ElementTree as ET

def inspect_headings(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        
        # Find all headings in content.xml
        for h in root.findall('.//text:h', namespaces):
            print(f"Heading: Tag={h.tag}, Attributes={h.attrib}")
            print(f"  Text: {''.join(h.itertext()).strip()}")

if __name__ == '__main__':
    inspect_headings(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
