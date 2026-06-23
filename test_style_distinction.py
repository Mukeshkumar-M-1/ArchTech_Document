import os
import zipfile
import shutil
import tempfile
import xml.etree.ElementTree as ET

def post_process_odt_distinguished(odt_path):
    temp_dir = tempfile.mkdtemp()
    try:
        # Extract ODT
        with zipfile.ZipFile(odt_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
            
        content_path = os.path.join(temp_dir, 'content.xml')
        styles_path = os.path.join(temp_dir, 'styles.xml')
        
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
        
        for prefix, uri in namespaces.items():
            ET.register_namespace(prefix, uri)
            
        for file_path in [content_path, styles_path]:
            if not os.path.exists(file_path):
                continue
                
            tree = ET.parse(file_path)
            root = tree.getroot()
            modified = False
            
            is_content_xml = (os.path.basename(file_path) == 'content.xml')
            
            if is_content_xml:
                auto_styles = root.find('office:automatic-styles', namespaces)
                if auto_styles is not None:
                    # Define custom styles to inject
                    custom_styles_to_inject = [
                        # 1. NavyTableHeaderCell
                        ('NavyTableHeaderCell', 'table-cell', {
                            'background-color': '#000080',
                            'border': '0.5pt solid #000000',
                            'padding-left': '0.075in',
                            'padding-right': '0.075in',
                            'padding-top': '0.04in',
                            'padding-bottom': '0.04in',
                            'vertical-align': 'middle'
                        }, 'style:table-cell-properties', None),
                        
                        # 2. NavyTableRowCell
                        ('NavyTableRowCell', 'table-cell', {
                            'background-color': 'transparent',
                            'border': '0.5pt solid #000000',
                            'padding-left': '0.075in',
                            'padding-right': '0.075in',
                            'padding-top': '0.04in',
                            'padding-bottom': '0.04in',
                            'vertical-align': 'middle'
                        }, 'style:table-cell-properties', None),
                        
                        # 3. GreyTableCell (matching Introduction table style)
                        ('GreyTableCell', 'table-cell', {
                            'background-color': '#dddddd',
                            'border': '0.5pt solid #ffffff',
                            'padding': '0.0382in',
                            'vertical-align': 'middle'
                        }, 'style:table-cell-properties', None),
                        
                        # 4. NavyTableHeadingText (paragraph style)
                        ('NavyTableHeadingText', 'paragraph', {
                            'color': '#ffffff',
                            'font-weight': 'bold',
                            'font-weight-asian': 'bold',
                            'font-weight-complex': 'bold',
                            'font-family': 'Arial',
                            'font-name': 'Arial',
                            'font-family-generic': 'swiss',
                            'font-pitch': 'variable'
                        }, 'style:text-properties', 'Table_20_Heading')
                    ]
                    
                    for name, family, attrs, prop_tag, parent_style_name in custom_styles_to_inject:
                        # Check if style already exists
                        exists = False
                        for s in auto_styles.findall('style:style', namespaces):
                            if s.get('{' + namespaces['style'] + '}name') == name:
                                exists = True
                                break
                                
                        if not exists:
                            s_elem = ET.Element('style:style')
                            s_elem.set('{' + namespaces['style'] + '}name', name)
                            s_elem.set('{' + namespaces['style'] + '}family', family)
                            if parent_style_name:
                                s_elem.set('{' + namespaces['style'] + '}parent-style-name', parent_style_name)
                                
                            p_elem = ET.Element(prop_tag)
                            for k, v in attrs.items():
                                if k in ['background-color', 'border', 'padding', 'padding-left', 'padding-right', 'padding-top', 'padding-bottom', 'color', 'font-weight', 'font-family']:
                                    p_elem.set('{' + namespaces['fo'] + '}' + k, v)
                                else:
                                    p_elem.set('{' + namespaces['style'] + '}' + k, v)
                                    
                            s_elem.append(p_elem)
                            auto_styles.append(s_elem)
                            modified = True
            
            # Modify general styles (Arial, 1.5 line spacing, Table_20_Heading black, Table shadows, justification)
            for style in root.findall('.//style:style', namespaces):
                name = style.get('{' + namespaces['style'] + '}name')
                family = style.get('{' + namespaces['style'] + '}family')
                
                # Set table drop shadows
                if family == 'table':
                    tp_elem = style.find('style:table-properties', namespaces)
                    if tp_elem is None:
                        tp_elem = ET.Element('style:table-properties')
                        style.append(tp_elem)
                    # Drop shadow: grey (#808080), offset by 0.04in right and down
                    tp_elem.set('{' + namespaces['style'] + '}shadow', '#808080 0.04in 0.04in')
                    modified = True
                
                # Check text-properties to set Font to Arial
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
                    
                # Check paragraph-properties to set line spacing to 150% and text alignment to justify
                if family == 'paragraph' and name not in ['Title', 'Subtitle', 'Heading', 'Table_20_Heading']:
                    if name is None or not name.startswith('Heading'):
                        pp = style.find('style:paragraph-properties', namespaces)
                        if pp is None:
                            pp = ET.Element('style:paragraph-properties')
                            style.append(pp)
                        pp.set('{' + namespaces['fo'] + '}line-height', '150%')
                        pp.set('{' + namespaces['fo'] + '}text-align', 'justify')
                        pp.set('{' + namespaces['style'] + '}justify-single-word', 'false')
                        modified = True
                        
                # Style Table_20_Heading (text inside normal headers) to BLACK, bold
                if name == 'Table_20_Heading' and family == 'paragraph':
                    tp = style.find('style:text-properties', namespaces)
                    if tp is None:
                        tp = ET.Element('style:text-properties')
                        style.append(tp)
                    tp.set('{' + namespaces['fo'] + '}color', '#000000') # Force black text for standard headers
                    tp.set('{' + namespaces['fo'] + '}font-weight', 'bold')
                    tp.set('{' + namespaces['style'] + '}font-weight-asian', 'bold')
                    tp.set('{' + namespaces['style'] + '}font-weight-complex', 'bold')
                    modified = True
            
            # Apply styles to tables by index in content.xml
            if is_content_xml:
                body = root.find('office:body', namespaces)
                if body is not None:
                    table_tag = "{" + namespaces['table'] + "}table"
                    table_cell_tag = "{" + namespaces['table'] + "}table-cell"
                    text_p_tag = "{" + namespaces['text'] + "}p"
                    
                    tables = body.findall('.//' + table_tag, namespaces)
                    print(f"Post-processing: Found {len(tables)} tables in body.")
                    
                    for idx, table in enumerate(tables):
                        is_navy_table = (idx in [0, 1])
                        
                        # Collect header rows and cells
                        header_rows = table.findall('.//table:table-header-rows', namespaces)
                        header_cells = set()
                        for hr in header_rows:
                            for cell in hr.findall('.//' + table_cell_tag, namespaces):
                                header_cells.add(cell)
                                
                        # Walk cells
                        for cell in table.findall('.//' + table_cell_tag, namespaces):
                            if cell in header_cells:
                                if is_navy_table:
                                    cell.set('{' + namespaces['table'] + '}style-name', 'NavyTableHeaderCell')
                                    for p in cell.findall('.//' + text_p_tag, namespaces):
                                        p.set('{' + namespaces['text'] + '}style-name', 'NavyTableHeadingText')
                                else:
                                    cell.set('{' + namespaces['table'] + '}style-name', 'GreyTableCell')
                                    for p in cell.findall('.//' + text_p_tag, namespaces):
                                        p.set('{' + namespaces['text'] + '}style-name', 'Table_20_Heading')
                            else:
                                if is_navy_table:
                                    cell.set('{' + namespaces['table'] + '}style-name', 'NavyTableRowCell')
                                    for p in cell.findall('.//' + text_p_tag, namespaces):
                                        p.set('{' + namespaces['text'] + '}style-name', 'Table_20_Contents')
                                else:
                                    cell.set('{' + namespaces['table'] + '}style-name', 'GreyTableCell')
                                    for p in cell.findall('.//' + text_p_tag, namespaces):
                                        p.set('{' + namespaces['text'] + '}style-name', 'Table_20_Contents')
                            modified = True
            
            if modified:
                tree.write(file_path, encoding='utf-8', xml_declaration=True)
                
        # Re-pack ODT zip file
        with zipfile.ZipFile(odt_path, 'w', zipfile.ZIP_DEFLATED) as zip_out:
            for root_dir, _, files in os.walk(temp_dir):
                for file in files:
                    full_p = os.path.join(root_dir, file)
                    rel_p = os.path.relpath(full_p, temp_dir)
                    zip_out.write(full_p, rel_p)
                    
        print(f"Processed and updated successfully: {odt_path}")
        
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    post_process_odt_distinguished(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
