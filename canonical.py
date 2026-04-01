import os
import re

CREATIONS_DIR = "./creations" 
BASE_URL = "https://chris-sta.github.io/my_failed_code/creations/"

def fix_canonicals():
    if not os.path.isdir(CREATIONS_DIR):
        print(f"Error: Could not find folder '{CREATIONS_DIR}'")
        return

    files_processed = 0
    tags_added = 0
    tags_updated = 0

    canonical_pattern = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']\s*/?>', re.IGNORECASE)

    for filename in os.listdir(CREATIONS_DIR):
        if filename.endswith(".html"):
            file_path = os.path.join(CREATIONS_DIR, filename)
            expected_url = f"{BASE_URL}{filename}"
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            existing_match = canonical_pattern.search(content)
            
            if existing_match:
                current_url = existing_match.group(1)
                if current_url == expected_url:
                    continue
                else:
                    new_tag = f'<link rel="canonical" href="{expected_url}" />'
                    new_content = canonical_pattern.sub(new_tag, content)
                    tags_updated += 1
            else:
                if "<head>" in content:
                    new_tag = f'\n<link rel="canonical" href="{expected_url}" />'
                    new_content = content.replace("<head>", f"<head>{new_tag}")
                    tags_added += 1
                else:
                    print(f"Skipping {filename}: No <head> tag found.")
                    continue

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            files_processed += 1

    print(f"--- Finished! ---")
    print(f"Total Files Checked: {files_processed}")
    print(f"New Tags Added:      {tags_added}")
    print(f"Tags Corrected:      {tags_updated}")

if __name__ == "__main__":
    fix_canonicals()