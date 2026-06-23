import zipfile
import xml.etree.ElementTree as ET

def find_font_and_spacing_in_styles(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        styles_xml = zip_ref.read('styles.xml')
        root = ET.fromstring(styles_xml)
        
        # ODF namespaces
        namespaces = {
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
        }
        
        # Print default styles or standard styles
        print("Styles defined in styles.xml:")
        for style in root.findall('.//style:style', namespaces)[:30]:
            name = style.get(f"{{{namespaces['style']}}}name")
            family = style.get(f"{{{namespaces['style']}}}family")
            
            # Find text properties
            tp = style.find('style:text-properties', namespaces)
            font_family = tp.get(f"{{{namespaces['fo']}}}font-family") if tp is not None else None
            
            # Find paragraph properties
            pp = style.find('style:paragraph-properties', namespaces)
            line_height = pp.get(f"{{{namespaces['fo']}}}line-height") if pp is not None else None
            
            if font_family or line_height:
                print(f"Style: '{name}' (Family: {family}) -> Font: {font_family}, Line Height: {line_height}")

if __name__ == "__main__":
    find_font_and_spacing_in_styles(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt")
