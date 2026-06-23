import zipfile
import xml.etree.ElementTree as ET

def dump_index_body(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        toc = root.find('.//text:table-of-content', namespaces)
        if toc is not None:
            index_body = toc.find('text:index-body', namespaces)
            if index_body is not None:
                print(f"Elements in index-body of {odt_path}: {len(index_body)}")
                for child in index_body:
                    text_style = '{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name'
                    style_val = child.get(text_style)
                    print(f"  Child tag: {child.tag}, style: {style_val}")
                    # Print text and structure of this child
                    print(f"    Text: {''.join(child.itertext())}")
                    # Let's serialize child to XML string
                    print(f"    XML: {ET.tostring(child, encoding='utf-8').decode('utf-8')[:300]}")
            else:
                print("index-body not found in TOC")
        else:
            print("TOC not found in ODT")

if __name__ == '__main__':
    dump_index_body(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
