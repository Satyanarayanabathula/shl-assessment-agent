id="v0t8rm"
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.shl.com"

CATALOG_URL = "https://www.shl.com/products/product-catalog/?f=1"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(CATALOG_URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")

assessment_links = []

for link in links:
    text = link.get_text(strip=True)
    href = link.get("href")

    if href and "/products/product-catalog/view/" in href:

        if not href.startswith("http"):
            href = BASE_URL + href

        assessment_links.append({
            "name": text,
            "url": href
        })

# remove duplicates
unique_assessments = []

seen_urls = set()

for assessment in assessment_links:
    if assessment["url"] not in seen_urls:
        seen_urls.add(assessment["url"])
        unique_assessments.append(assessment)

print("TOTAL ASSESSMENTS:", len(unique_assessments))

all_data = []

for assessment in unique_assessments:

    print("SCRAPING:", assessment["name"])

    try:
        detail_response = requests.get(
            assessment["url"],
            headers=headers
        )

        detail_soup = BeautifulSoup(
            detail_response.text,
            "html.parser"
        )

        page_text = detail_soup.get_text(
            separator=" ",
            strip=True
        )

        all_data.append({
            "name": assessment["name"],
            "url": assessment["url"],
            "description": page_text[:5000]
        })

        time.sleep(1)

    except Exception as e:
        print("ERROR:", e)

df = pd.DataFrame(all_data)

df.to_csv("data/shl_assessments.csv", index=False)

print("DATASET SAVED")
print(df.head())

