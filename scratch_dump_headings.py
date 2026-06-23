import zipfile
import xml.etree.ElementTree as ET

def dump_headings(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    print(f"\n=== Headings in {odt_path} ===")
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        for h in root.findall('.//text:h', namespaces):
            text_content = "".join(h.itertext()).strip()
            level = h.get(f"{{{namespaces['text']}}}outline-level")
            style_name = h.get(f"{{{namespaces['text']}}}style-name")
            print(f"Level: {level}, Style: {style_name} -> '{text_content}'")

if __name__ == '__main__':
    dump_headings(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
    dump_headings(r"SRS_DEMO_SECTION\SRS_TEST_2.odt")
