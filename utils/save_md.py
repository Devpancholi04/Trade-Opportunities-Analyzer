import os

def save_md_file(sector, report):
    os.makedirs('reports', exist_ok=True)
    filename = f"reports/{sector} report.md"
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(report)
    return filename