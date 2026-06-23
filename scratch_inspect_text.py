import zipfile
import xml.etree.ElementTree as ET

def find_text_in_template(odt_path, query):
    namespaces = {
        'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
        'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    }
    
    with zipfile.ZipFile(odt_path, 'r') as zip_ref:
        content_xml = zip_ref.read('content.xml')
        root = ET.fromstring(content_xml)
        
        # search for any element containing the query text
        found = []
        for elem in root.iter():
            text = "".join(elem.itertext())
            if query.lower() in text.lower():
                found.append((elem.tag, elem.attrib, text.strip()))
                
        print(f"Matches for '{query}': {len(found)}")
        for idx, item in enumerate(found[:20]):
            print(f"{idx+1}: Tag={item[0].split('}')[-1]} Attrib={item[1]} -> '{item[2][:100]}'")

if __name__ == "__main__":
    find_text_in_template(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt", "DOCUMENT CONTROL")
    find_text_in_template(r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt", "REVISION HISTORY")
