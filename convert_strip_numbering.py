import re
import sys
import subprocess
import os

def strip_heading_numbering(md_content):
    # Regex to match Markdown headings with numbers: e.g. "## 1. INTRODUCTION" or "### 1.1 Purpose"
    # Matches:
    # 1. Start of line
    # 2. One or more hashes (#+)
    # 3. Leading whitespace (\s+)
    # 4. Numbers separated by dots (e.g., 1.2.3 or 1.)
    # 5. Whitespace (\s+)
    # 6. Heading text
    pattern = re.compile(r'^(#+)\s+(\d+(?:\.\d+)*\.?)\s+(.*)$')
    
    lines = md_content.splitlines()
    new_lines = []
    for line in lines:
        match = pattern.match(line)
        if match:
            hashes = match.group(1)
            heading_text = match.group(3)
            new_lines.append(f"{hashes} {heading_text}")
        else:
            new_lines.append(line)
            
    return "\n".join(new_lines)

def convert_md_to_odt(input_md, output_odt, template_odt):
    # Read original markdown
    with open(input_md, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip heading numbering
    clean_content = strip_heading_numbering(content)
    
    # Save to a temporary markdown file
    temp_md = input_md + ".temp.md"
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(clean_content)
        
    try:
        # Run pandoc conversion
        cmd = [
            'pandoc', '-s',
            '-f', 'markdown',
            '-t', 'odt',
            '--reference-doc', template_odt,
            '-o', output_odt,
            temp_md
        ]
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Pandoc conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during pandoc conversion: {e.stderr}")
    finally:
        # Clean up temporary markdown file
        if os.path.exists(temp_md):
            os.remove(temp_md)

if __name__ == "__main__":
    template = r"d:\ArchTech_AI\_V5\Pandoc_working\DP-XMC-5049-000-V1-01-SRS-0V03.odt"
    input_file = r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1.md"
    output_file = r"d:\ArchTech_AI\_V5\Pandoc_working\SRS_DEMO_SECTION\SRS_TEST_1_clean.odt"
    
    convert_md_to_odt(input_file, output_file, template)
