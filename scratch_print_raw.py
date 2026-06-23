import zipfile
import xml.etree.ElementTree as ET

def print_raw_headings(odt_path):
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        
        namespaces = {
            'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
        }
        
        # Find elements of text:h
        for elem in root.findall('.//text:h', namespaces)[:10]:
            print(ET.tostring(elem, encoding='utf-8').decode('utf-8'))

if __name__ == "__main__":
    print_raw_headings(r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.odt")
