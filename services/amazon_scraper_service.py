import requests
from bs4 import BeautifulSoup

def scrape_products(keyword):

    url = f"https://www.amazon.com/s?k={keyword.replace(' ','+')}"

    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    products = []

    results = soup.select(".s-result-item")[:5]

    for item in results:

        title = item.select_one("h2")

        link = item.select_one("a")

        if title and link:

            products.append({
                "title": title.text.strip(),
                "url": "https://www.amazon.com" + link["href"]
            })

    return products
