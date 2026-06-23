import zipfile
import xml.etree.ElementTree as ET

def find_specific_table_styles(odt_path):
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
        
        # Find Table1 definition
        body = root.find('office:body', namespaces)
        if body is None:
            return
            
        table_tag = "{" + namespaces['table'] + "}table"
        table_row_tag = "{" + namespaces['table'] + "}table-row"
        table_cell_tag = "{" + namespaces['table'] + "}table-cell"
        
        table1 = None
        for table in body.findall('.//' + table_tag, namespaces):
            name = table.get("{" + namespaces['table'] + "}name")
            # Let's print the first few tables we find
            print(f"Table name: '{name}'")
            # Let's look at the first row and cell styles
            first_row = table.find('.//' + table_row_tag, namespaces)
            if first_row is not None:
                cells = first_row.findall('.//' + table_cell_tag, namespaces)
                cell_styles = [c.get("{" + namespaces['table'] + "}style-name") for c in cells]
                print(f"  First row cell styles: {cell_styles}")
                
            second_row = table.findall('.//' + table_row_tag, namespaces)
            if len(second_row) > 1:
                cells = second_row[1].findall('.//' + table_cell_tag, namespaces)
                cell_styles = [c.get("{" + namespaces['table'] + "}style-name") for c in cells]
                print(f"  Second row cell styles: {cell_styles}")

if __name__ == "__main__":
    find_specific_table_styles(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt")
