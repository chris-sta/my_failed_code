import os
from datetime import datetime

BASE_URL = "https://chris-sta.github.io/my_failed_code/" 
EXCLUDE = ['404.html', 'hinventory.html'] 

def generate_sitemap():
    pages = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html") and file not in EXCLUDE:
                rel_path = os.path.relpath(os.path.join(root, file), ".")
                url_path = rel_path.replace("\\", "/")
                
                if url_path == "index.html":
                    full_url = BASE_URL
                elif url_path.endswith("index.html"):
                    full_url = BASE_URL + url_path[:-10]
                else:
                    full_url = BASE_URL + url_path
                
                pages.append(full_url)

    now = datetime.now().strftime("%Y-%m-%d")
    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in pages:
        xml_content.append('  <url>')
        xml_content.append(f'    <loc>{page}</loc>')
        xml_content.append(f'    <lastmod>{now}</lastmod>')
        xml_content.append('    <changefreq>monthly</changefreq>')
        xml_content.append('  </url>')

    xml_content.append('</urlset>')

    with open("sitemap_index.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(xml_content))
    
    print(f"Done! Successfully mapped {len(pages)} pages to sitemap.xml")

if __name__ == "__main__":
    generate_sitemap()