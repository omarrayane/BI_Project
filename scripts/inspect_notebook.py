import json
import re

def inspect_notebook(filepath, output_path):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    with open(output_path, 'w', encoding='utf-8') as out:
        for i, cell in enumerate(nb['cells']):
            if cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                if 'px.' in source or 'go.' in source or 'color' in source or 'fig' in source:
                    out.write(f"--- Cell {i} ---\n")
                    out.write(source + "\n")
                    out.write("----------------\n")

if __name__ == "__main__":
    inspect_notebook(r"C:\Users\HP\OneDrive\Bureau\Projet-BI\notebooks\visualization_interactive.ipynb", "notebook_source.txt")
