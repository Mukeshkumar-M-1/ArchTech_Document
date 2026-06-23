import zipfile
import xml.etree.ElementTree as ET

def inspect_generated_tables(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        
        namespaces = {
            'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
            'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
        }
        
        print("=== Generated Tables in content.xml ===")
        # Print table styles in automatic-styles
        auto_styles = root.find('office:automatic-styles', namespaces)
        if auto_styles is not None:
            for style in auto_styles.findall('style:style', namespaces):
                family = style.get(f"{{{namespaces['style']}}}family")
                name = style.get(f"{{{namespaces['style']}}}name")
                if family in ['table', 'table-column', 'table-row', 'table-cell']:
                    print(f"Auto Style: {name} (Family: {family})")
                    # print attributes of properties
                    for prop in style:
                        tag_name = prop.tag.split('}')[-1]
                        print(f"  {tag_name}: {prop.attrib}")
                        
        # Let's inspect the actual table markup
        body = root.find('office:body', namespaces)
        if body is not None:
            table_tag = "{" + namespaces['table'] + "}table"
            style_name_tag = "{" + namespaces['table'] + "}style-name"
            style_name_style_tag = "{" + namespaces['style'] + "}style-name"
            for table in body.findall('.//' + table_tag, namespaces)[:2]:
                print(f"Table in body: style-name={table.get(style_name_tag)}")
                for child in table[:5]:
                    c_tag = child.tag.split('}')[-1]
                    c_style = child.get(style_name_tag) or child.get(style_name_style_tag)
                    print(f"  Child tag: {c_tag}, style-name={c_style}")
                    # If it's a row, check cell styles
                    if child.tag.endswith('table-row'):
                        for cell in child[:3]:
                            cell_tag = cell.tag.split('}')[-1]
                            cell_style = cell.get(style_name_tag)
                            print(f"    Cell tag: {cell_tag}, style-name={cell_style}")

if __name__ == "__main__":
    inspect_generated_tables(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
