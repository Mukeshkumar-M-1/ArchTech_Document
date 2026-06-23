import zipfile
import xml.etree.ElementTree as ET

def dump_xml_structure(odt_path, filename):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        xml_data = zip_ref.read(filename)
        root = ET.fromstring(xml_data)
        
        namespaces = {
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
        }
        
        print(f"=== Styles in {filename} ===")
        # Print styles that contain paragraph-properties or table-cell-properties
        for style in root.findall('.//style:style', namespaces):
            name = style.get(f"{{{namespaces['style']}}}name")
            family = style.get(f"{{{namespaces['style']}}}family")
            
            # Print child element tags
            children = [c.tag.split('}')[-1] for c in style]
            
            # Check paragraph-properties
            pp = style.find('style:paragraph-properties', namespaces)
            pp_attrs = pp.attrib if pp is not None else None
            
            # Check text-properties
            tp = style.find('style:text-properties', namespaces)
            tp_attrs = tp.attrib if tp is not None else None
            
            # Check table-cell-properties
            tcp = style.find('style:table-cell-properties', namespaces)
            tcp_attrs = tcp.attrib if tcp is not None else None
            
            if name in ['Standard', 'Text_20_body', 'Table_20_Contents', 'Table_20_Heading'] or family in ['table', 'table-column', 'table-row', 'table-cell']:
                print(f"Name: {name}, Family: {family}, Children: {children}")
                if pp_attrs: print(f"  PP Attrs: {pp_attrs}")
                if tp_attrs: print(f"  TP Attrs: {tp_attrs}")
                if tcp_attrs: print(f"  TCP Attrs: {tcp_attrs}")

if __name__ == "__main__":
    dump_xml_structure(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt", 'styles.xml')
    dump_xml_structure(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt", 'content.xml')
