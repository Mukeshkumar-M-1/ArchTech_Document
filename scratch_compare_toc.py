import zipfile
import xml.etree.ElementTree as ET

def get_toc_xml(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        toc = root.find('.//text:table-of-content', namespaces)
        if toc is not None:
            return ET.tostring(toc, encoding='utf-8').decode('utf-8')
        return None

def main():
    template_toc = get_toc_xml("DP-XMC-5049-000-V1-01-SRS-0V03.odt")
    generated_toc = get_toc_xml(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
    
    print("--- TEMPLATE TOC ---")
    print(template_toc[:2000] if template_toc else "None")
    print("\n--- GENERATED TOC ---")
    print(generated_toc[:2000] if generated_toc else "None")

if __name__ == '__main__':
    main()
