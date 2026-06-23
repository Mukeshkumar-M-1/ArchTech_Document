import os
import zipfile
import shutil
import tempfile
import xml.etree.ElementTree as ET

def post_process_odt(odt_path):
    temp_dir = tempfile.mkdtemp()
    try:
        # Extract the ODT file
        with zipfile.ZipFile(odt_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            
        content_path = os.path.join(temp_dir, 'content.xml')
        styles_path = os.path.join(temp_dir, 'styles.xml')
        
        # ODF namespaces
        namespaces = {
            'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
            'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
            'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
            'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
            'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
            'svg': 'urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0',
            'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
            'meta': 'urn:oasis:names:tc:opendocument:xmlns:meta:1.0',
            'number': 'urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0',
            'dc': 'http://purl.org/dc/elements/1.1/',
        }
        
        # Register namespaces to prevent ns0, ns1 prefixes
        for prefix, uri in namespaces.items():
            ET.register_namespace(prefix, uri)
            
        # 1. First, modify styles.xml and content.xml style definitions
        for file_path in [content_path, styles_path]:
            if not os.path.exists(file_path):
                continue
                
            tree = ET.parse(file_path)
            root = tree.getroot()
            modified = False
            
            # Find or create automatic-styles or styles tag to add TableHeaderCell style if it's content.xml
            is_content_xml = (os.path.basename(file_path) == 'content.xml')
            
            if is_content_xml:
                auto_styles = root.find('office:automatic-styles', namespaces)
                if auto_styles is not None:
                    # Check if TableHeaderCell is already there
                    thc_exists = False
                    for style in auto_styles.findall('style:style', namespaces):
                        name = style.get('{' + namespaces['style'] + '}name')
                        if name == 'TableHeaderCell':
                            thc_exists = True
                            break
                            
                    if not thc_exists:
                        # Create TableHeaderCell style
                        thc_style = ET.Element('style:style')
                        thc_style.set('{' + namespaces['style'] + '}name', 'TableHeaderCell')
                        thc_style.set('{' + namespaces['style'] + '}family', 'table-cell')
                        
                        thc_props = ET.Element('style:table-cell-properties')
                        thc_props.set('{' + namespaces['fo'] + '}background-color', '#1F2937')  # Dark gray
                        thc_props.set('{' + namespaces['fo'] + '}border', '0.5pt solid #4B5563')  # Slate border
                        thc_props.set('{' + namespaces['fo'] + '}padding', '0.08in')
                        thc_props.set('{' + namespaces['style'] + '}vertical-align', 'middle')
                        
                        thc_style.append(thc_props)
                        auto_styles.append(thc_style)
                        modified = True
            
            # Find and update existing style definitions
            for style in root.findall('.//style:style', namespaces):
                name = style.get('{' + namespaces['style'] + '}name')
                family = style.get('{' + namespaces['style'] + '}family')
                
                # Update text font to Arial
                tp = style.find('style:text-properties', namespaces)
                if tp is not None:
                    tp.set('{' + namespaces['fo'] + '}font-family', 'Arial')
                    tp.set('{' + namespaces['style'] + '}font-name', 'Arial')
                    tp.set('{' + namespaces['style'] + '}font-family-generic', 'swiss')
                    tp.set('{' + namespaces['style'] + '}font-pitch', 'variable')
                    tp.set('{' + namespaces['style'] + '}font-name-asian', 'Arial')
                    tp.set('{' + namespaces['style'] + '}font-family-asian', 'Arial')
                    tp.set('{' + namespaces['style'] + '}font-name-complex', 'Arial')
                    tp.set('{' + namespaces['style'] + '}font-family-complex', 'Arial')
                    modified = True
                    
                # Update paragraph line-height to 150% (1.5 line spacing)
                # Exclude Title, Subtitle, and Headings
                if family == 'paragraph' and name not in ['Title', 'Subtitle', 'Heading']:
                    if name is None or not name.startswith('Heading'):
                        pp = style.find('style:paragraph-properties', namespaces)
                        if pp is None:
                            pp = ET.Element('style:paragraph-properties')
                            style.append(pp)
                        pp.set('{' + namespaces['fo'] + '}line-height', '150%')
                        modified = True
                        
                # Style body cell (TableRowCell)
                if name == 'TableRowCell' and family == 'table-cell':
                    tcp = style.find('style:table-cell-properties', namespaces)
                    if tcp is None:
                        tcp = ET.Element('style:table-cell-properties')
                        style.append(tcp)
                    tcp.set('{' + namespaces['fo'] + '}background-color', 'transparent')
                    tcp.set('{' + namespaces['fo'] + '}border', '0.5pt solid #D1D5DB')
                    tcp.set('{' + namespaces['fo'] + '}padding', '0.08in')
                    tcp.set('{' + namespaces['style'] + '}vertical-align', 'middle')
                    modified = True
                    
                # Style Table_20_Heading (text inside header) to white color, bold
                if name == 'Table_20_Heading' and family == 'paragraph':
                    tp = style.find('style:text-properties', namespaces)
                    if tp is None:
                        tp = ET.Element('style:text-properties')
                        style.append(tp)
                    tp.set('{' + namespaces['fo'] + '}color', '#FFFFFF')
                    tp.set('{' + namespaces['fo'] + '}font-weight', 'bold')
                    tp.set('{' + namespaces['style'] + '}font-weight-asian', 'bold')
                    tp.set('{' + namespaces['style'] + '}font-weight-complex', 'bold')
                    modified = True
                    
            # 3. For content.xml, find cell elements inside table-header-rows and set their style to TableHeaderCell
            if is_content_xml:
                body = root.find('office:body', namespaces)
                if body is not None:
                    # Find all table:table-header-rows elements
                    for header_rows in body.findall('.//table:table-header-rows', namespaces):
                        # Find all table:table-cell elements in it
                        for cell in header_rows.findall('.//table:table-cell', namespaces):
                            cell.set('{' + namespaces['table'] + '}style-name', 'TableHeaderCell')
                            modified = True
            
            if modified:
                tree.write(file_path, encoding='utf-8', xml_declaration=True)
                
        # Re-pack the ODT zip file
        with zipfile.ZipFile(odt_path, 'w', zipfile.ZIP_DEFLATED) as zip_out:
            for root_dir, _, files in os.walk(temp_dir):
                for file in files:
                    full_p = os.path.join(root_dir, file)
                    rel_p = os.path.relpath(full_p, temp_dir)
                    zip_out.write(full_p, rel_p)
                    
        print(f"Successfully processed and updated: {odt_path}")
                    
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    post_process_odt(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
