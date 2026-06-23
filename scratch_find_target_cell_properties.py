import zipfile
import xml.etree.ElementTree as ET

def find_target_cell_properties(odt_path, target_styles):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        
        namespaces = {
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
        }
        
        for style in root.findall('.//style:style', namespaces):
            name = style.get("{" + namespaces['style'] + "}name")
            if name in target_styles:
                print(f"Style: {name}")
                tcp = style.find('style:table-cell-properties', namespaces)
                if tcp is not None:
                    for k, v in tcp.attrib.items():
                        print(f"  {k.split('}')[-1]} = {v}")

if __name__ == "__main__":
    targets = [
        'Table1.A1', 'Table1.A2',
        'Table2.A1', 'Table2.A2',
        'Table11.A1', 'Table11.A2',
        'Table12.A1', 'Table12.A2',
        'Table13.A1', 'Table13.A2'
    ]
    find_target_cell_properties(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt", targets)
