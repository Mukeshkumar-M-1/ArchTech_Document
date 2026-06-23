import zipfile
import xml.etree.ElementTree as ET

def find_cell_styles_in_template(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        for filename in ['styles.xml', 'content.xml']:
            xml_data = zip_ref.read(filename)
            root = ET.fromstring(xml_data)
            
            namespaces = {
                'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
                'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
            }
            
            style_family_tag = "{" + namespaces['style'] + "}family"
            for style in root.findall('.//style:style', namespaces):
                name = style.get("{" + namespaces['style'] + "}name")
                if name in ['TableRowCell', 'TableHeaderCell', 'Table', 'Table_20_Contents', 'Table_20_Heading']:
                    print(f"Found style in {filename}: Name='{name}' Family='{style.get(style_family_tag)}'")
                    # Print properties
                    for prop in style:
                        print(f"  {prop.tag.split('}')[-1]}: {prop.attrib}")

if __name__ == "__main__":
    find_cell_styles_in_template(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt")
