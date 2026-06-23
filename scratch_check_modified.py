import zipfile
import xml.etree.ElementTree as ET

def check_modified_styles(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        for filename in ['content.xml', 'styles.xml']:
            xml_data = zip_ref.read(filename)
            root = ET.fromstring(xml_data)
            
            namespaces = {
                'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
                'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
            }
            
            for style in root.findall('.//style:style', namespaces):
                name = style.get(f"{{{namespaces['style']}}}name")
                if name in ['Table_20_Contents', 'Text_20_body', 'Standard']:
                    print(f"Style: {name} in {filename}")
                    pp = style.find('style:paragraph-properties', namespaces)
                    if pp is not None:
                        for k, v in pp.attrib.items():
                            print(f"  PP: {k.split('}')[-1]} = {v}")
                    tp = style.find('style:text-properties', namespaces)
                    if tp is not None:
                        for k, v in tp.attrib.items():
                            print(f"  TP: {k.split('}')[-1]} = {v}")

if __name__ == "__main__":
    check_modified_styles(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
