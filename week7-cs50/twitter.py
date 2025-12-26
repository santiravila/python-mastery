import re

url = input("URL: ").strip()

pattern = r"^https?://(?:www\.)?twitter\.com/(\w+)"
if matches := re.search(pattern, url, re.IGNORECASE):
    print(f"Usarname: {matches.group(1)}")