import json
import re

def update_notebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    changes_count = 0

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            source_list = cell['source']
            source_text = "".join(source_list)
            
            # Helper to check if we are in a specific cell context
            is_country_bar = "title='Total Orders by Country'" in source_text
            is_3d_scatter = "title='OLAP View:" in source_text
            is_pie = "type='pie'" in source_text or "go.Pie" in source_text
            
            for line in source_list:
                original_line = line
                
                # 1. Update Pie Colors (Global or Context Specific)
                if "colors=['#2ecc71', '#e74c3c']" in line:
                    line = line.replace("colors=['#2ecc71', '#e74c3c']", "colors=['#10b981', '#f43f5e']")
                
                # 2. Update Viridis Scale
                # Context 1: Country Bar -> Tealgrn
                if "color_continuous_scale='Viridis'" in line and is_country_bar:
                   line = line.replace("'Viridis'", "'Tealgrn'")
                # Context 2: 3D Scatter -> Turbo
                elif "color_continuous_scale='Viridis'" in line and is_3d_scatter:
                   line = line.replace("'Viridis'", "'Turbo'")
                
                # 3. Update Plasma Scale -> Purples
                if "color_continuous_scale='Plasma'" in line:
                    line = line.replace("'Plasma'", "'Purples'")
                
                # 4. Update Line Color (Monthly Trend)
                if "line=dict(color='#3498db', width=3)" in line:
                    line = line.replace("'#3498db'", "'#6366f1'")
                
                # 5. Update Delivery Status Bar Colors
                if "color_discrete_map={'Delivered': '#2ecc71', 'Not Delivered': '#e74c3c'}" in line:
                    line = line.replace("'#2ecc71'", "'#10b981'").replace("'#e74c3c'", "'#f43f5e'")
                
                # 6. Dashboard Subplots
                if "marker=dict(color='#3498db'))" in line:
                    line = line.replace("'#3498db'", "'#06b6d4'")
                
                if "line=dict(color='#9b59b6')" in line:
                    line = line.replace("'#9b59b6'", "'#f43f5e'")
                    
                if "marker=dict(color='#e67e22')" in line:
                    line = line.replace("'#e67e22'", "'#f59e0b'")
                
                # 7. Add color_discrete_map to px.bar calls for delivery status (Cell 20)
                # This is trickier as it needs insertion.
                # We look for the specific px.bar call and inject the argument.
                if "fig_emp = px.bar(emp_delivery, x='LastName', y='Count', color='Status'," in line:
                    line = line.replace(
                        "fig_emp = px.bar(emp_delivery, x='LastName', y='Count', color='Status',",
                        "fig_emp = px.bar(emp_delivery, x='LastName', y='Count', color='Status', color_discrete_map={'Delivered': '#10b981', 'Not Delivered': '#f43f5e'},"
                    )

                if "fig_country = px.bar(country_delivery, x='Country_x', y='Count', color='Status'," in line:
                    line = line.replace(
                        "fig_country = px.bar(country_delivery, x='Country_x', y='Count', color='Status',",
                        "fig_country = px.bar(country_delivery, x='Country_x', y='Count', color='Status', color_discrete_map={'Delivered': '#10b981', 'Not Delivered': '#f43f5e'},"
                    )

                if line != original_line:
                    changes_count += 1
                
                new_source.append(line)
            
            cell['source'] = new_source

    print(f"Total changes applied: {changes_count}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=4)

if __name__ == "__main__":
    update_notebook(r"C:\Users\HP\OneDrive\Bureau\Projet-BI\notebooks\visualization_interactive.ipynb")
