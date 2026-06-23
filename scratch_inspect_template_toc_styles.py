import zipfile
import xml.etree.ElementTree as ET

def inspect_styles(odt_path):
    namespaces = {
        'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    
    with zipfile.ZipFile(odt_path, 'r') as z:
        # Search content.xml automatic-styles for P37, P38, P39, P40
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        
        style_parent_attr = '{urn:oasis:names:tc:opendocument:xmlns:style:1.0}parent-style-name'
        target_styles = ['P37', 'P38', 'P39', 'P40']
        for style in root.findall('.//style:style', namespaces):
            name = style.get(f"{{{namespaces['style']}}}name")
            if name in target_styles:
                print(f"Style: {name}, Parent: {style.get(style_parent_attr)}")
                pp = style.find('style:paragraph-properties', namespaces)
                if pp is not None:
                    print(f"  Paragraph properties attributes: {pp.attrib}")
                    # Print tab-stops if any
                    tabs = pp.find('style:tab-stops', namespaces)
                    if tabs is not None:
                        for tab in tabs:
                            print(f"    Tab Stop: {tab.attrib}")
                tp = style.find('style:text-properties', namespaces)
                if tp is not None:
                    print(f"  Text properties attributes: {tp.attrib}")

if __name__ == '__main__':
    inspect_styles("DP-XMC-5049-000-V1-01-SRS-0V03.odt")
