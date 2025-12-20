import os
import re

BASE_DIR = r"C:\Users\HP\OneDrive\Bureau\Projet-BI\report"
OUTPUT_FILE = r"C:\Users\HP\OneDrive\Bureau\Projet-BI\report\full_report_flattened.tex"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def flatten_latex():
    # 1. Read Main
    main_content = read_file(os.path.join(BASE_DIR, "main.tex"))
    
    # 2. Inject Bibliography via filecontents
    bib_content = read_file(os.path.join(BASE_DIR, "references.bib"))
    bib_injection = "\\begin{filecontents}{references.bib}\n" + bib_content + "\n\\end{filecontents}\n"
    
    # Insert before \documentclass
    final_content = bib_injection + main_content
    
    # 3. Replace \input{settings/packages}
    pkg_content = read_file(os.path.join(BASE_DIR, "settings", "packages.tex"))
    final_content = final_content.replace("\\input{settings/packages}", pkg_content)
    
    # 4. Replace Chapters
    # Regex to find \input{chapters/filename}
    # Note: filenames might or might not have .tex extension in the input command
    # In my generator I used \input{chapters/00_abstract} without extension
    
    def replacer(match):
        filename = match.group(1)
        if not filename.endswith('.tex'):
            filename += ".tex"
        
        chapter_path = os.path.join(BASE_DIR, "chapters", filename)
        if os.path.exists(chapter_path):
            return read_file(chapter_path)
        else:
            return f"% ERROR: File {filename} not found"

    final_content = re.sub(r"\\input\{chapters/([^}]+)\}", replacer, final_content)
    
    # 5. Write Output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"Flattened report written to {OUTPUT_FILE}")

if __name__ == "__main__":
    flatten_latex()
