import zipfile
import xml.etree.ElementTree as ET

def verify_table_shadows(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        
        namespaces = {
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
        }
        
        print("Checking Table Styles for shadows...")
        for style in root.findall('.//style:style', namespaces):
            family = style.get(f"{{{namespaces['style']}}}family")
            if family == 'table':
                name = style.get(f"{{{namespaces['style']}}}name")
                print(f"Table Style: {name}")
                tp = style.find('style:table-properties', namespaces)
                if tp is not None:
                    for k, v in tp.attrib.items():
                        print(f"  {k.split('}')[-1]} = {v}")

if __name__ == "__main__":
    verify_table_shadows(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
