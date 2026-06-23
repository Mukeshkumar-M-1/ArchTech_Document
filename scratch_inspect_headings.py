import zipfile
import xml.etree.ElementTree as ET

def check_file(odt_path):
    namespaces = {
        'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'fo': 'urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    
    # Store break-before attribute for each style name
    style_page_breaks = {}
    
    with zipfile.ZipFile(odt_path, 'r') as z:
        # 1. Parse styles.xml and content.xml to collect all style break-before definitions
        for filename in ['styles.xml', 'content.xml']:
            xml_data = z.read(filename)
            root = ET.fromstring(xml_data)
            for style in root.findall('.//style:style', namespaces):
                name = style.get(f"{{{namespaces['style']}}}name")
                pp = style.find('style:paragraph-properties', namespaces)
                if pp is not None:
                    break_before = pp.get(f"{{{namespaces['fo']}}}break-before")
                    if break_before == 'page':
                        style_page_breaks[name] = True
                        
        # 2. Scan headings and heading-styled paragraphs in content.xml
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        print(f"\nVerification for {odt_path}:")
        
        for child in root.iter():
            if child.tag in [f"{{{namespaces['text']}}}h", f"{{{namespaces['text']}}}p"]:
                style_name = child.get(f"{{{namespaces['text']}}}style-name")
                if style_name and ('Heading' in style_name or 'PageBreak' in style_name):
                    text_content = "".join(child.itertext()).strip()
                    tag_type = "text:h" if child.tag.endswith('h') else "text:p"
                    level = child.get(f"{{{namespaces['text']}}}outline-level", "N/A")
                    has_break = style_page_breaks.get(style_name, False)
                    break_status = "[PAGE BREAK]" if has_break else "[NO BREAK]"
                    print(f"  Element: {tag_type:6} Level: {level:3} {break_status} (Style: {style_name:20}) -> '{text_content}'")

def main():
    check_file(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
    check_file(r"SRS_DEMO_SECTION\SRS_TEST_2.odt")

if __name__ == '__main__':
    main()
