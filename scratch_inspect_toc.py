import zipfile
import xml.etree.ElementTree as ET

def check_toc(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        toc = root.find('.//text:table-of-content', namespaces)
        if toc is not None:
            print(f"Main TOC Element: {toc.tag}, Attributes: {toc.attrib}")
            source = toc.find('text:table-of-content-source', namespaces)
            if source is not None:
                print(f"Source Element: {source.tag}, Attributes: {source.attrib}")
                title_template = source.find('text:index-title-template', namespaces)
                if title_template is not None:
                    print(f"  Title Template Element: {title_template.tag}, Attributes: {title_template.attrib}")
                    print(f"    Text: {title_template.text}")
            
            index_body = toc.find('text:index-body', namespaces)
            if index_body is not None:
                print(f"Index Body Element: {index_body.tag}, Attributes: {index_body.attrib}")
                h_elem = index_body.find('text:index-title', namespaces)
                if h_elem is not None:
                    print(f"  Index Title under Index Body: {h_elem.tag}, Attributes: {h_elem.attrib}")
                    print(f"    Text: {''.join(h_elem.itertext())}")
            else:
                print("No index-body found under TOC")
        else:
            print(f"No TOC found in {odt_path}")

if __name__ == '__main__':
    check_toc(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
    check_toc(r"SRS_DEMO_SECTION\SRS_TEST_2.odt")
