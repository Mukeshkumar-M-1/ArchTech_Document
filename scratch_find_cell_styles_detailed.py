import zipfile
import xml.etree.ElementTree as ET

def find_cell_styles_detailed(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        for filename in ['content.xml']:
            xml_data = zip_ref.read(filename)
            root = ET.fromstring(xml_data)
            
            namespaces = {
                'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
                'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
            }
            
            style_family_tag = "{" + namespaces['style'] + "}family"
            style_name_tag = "{" + namespaces['style'] + "}name"
            
            cell_styles = []
            for style in root.findall('.//style:style', namespaces):
                family = style.get(style_family_tag)
                if family == 'table-cell':
                    name = style.get(style_name_tag)
                    tcp = style.find('style:table-cell-properties', namespaces)
                    if tcp is not None:
                        cell_styles.append((name, tcp.attrib))
                        
            print(f"Total table-cell styles in {filename}: {len(cell_styles)}")
            # Let's group them or look at common properties
            # Print first 20 styles
            for name, attrs in cell_styles[:20]:
                print(f"Cell Style '{name}':")
                for k, v in attrs.items():
                    print(f"  {k.split('}')[-1]} = {v}")

if __name__ == "__main__":
    find_cell_styles_detailed(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt")
