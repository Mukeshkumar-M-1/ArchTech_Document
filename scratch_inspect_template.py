import zipfile
import xml.etree.ElementTree as ET

def check_template_headings(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        headings = root.findall('.//text:h', namespaces)
        print(f"Total headings in template: {len(headings)}")
        for idx, h in enumerate(headings[:20]):
            text_content = "".join(h.itertext())
            outline_level = h.get(f"{{{namespaces['text']}}}outline-level", "N/A")
            style_name = h.get(f"{{{namespaces['text']}}}style-name", "N/A")
            print(f"Heading {idx+1}: Level {outline_level} (Style: {style_name}) -> '{text_content}'")

if __name__ == "__main__":
    check_template_headings(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt")
