import zipfile
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def get_toc_element(odt_path):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    with zipfile.ZipFile(odt_path, 'r') as z:
        content_xml = z.read('content.xml')
        root = ET.fromstring(content_xml)
        toc = root.find('.//text:table-of-content', namespaces)
        return toc

def prettify(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def main():
    template_toc = get_toc_element("DP-XMC-5049-000-V1-01-SRS-0V03.odt")
    generated_toc = get_toc_element(r"SRS_DEMO_SECTION\SRS_TEST_1.odt")
    
    if template_toc is not None:
        with open("scratch_template_toc_pretty.xml", "w", encoding="utf-8") as f:
            f.write(prettify(template_toc))
        print("Wrote template TOC to scratch_template_toc_pretty.xml")
    else:
        print("Template TOC not found")
        
    if generated_toc is not None:
        with open("scratch_generated_toc_pretty.xml", "w", encoding="utf-8") as f:
            f.write(prettify(generated_toc))
        print("Wrote generated TOC to scratch_generated_toc_pretty.xml")
    else:
        print("Generated TOC not found")

if __name__ == '__main__':
    main()
