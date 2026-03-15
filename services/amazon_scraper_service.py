from playwright.sync_api import sync_playwright


def scrape_amazon_products(keyword):

    url = f"https://www.amazon.com/s?k={keyword.replace(' ','+')}"

    products = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        )

        page = context.new_page()

        page.goto(url)

        page.wait_for_selector("div[data-component-type='s-search-result']")
        page.wait_for_timeout(2000)

        items = page.query_selector_all("div[data-component-type='s-search-result']")

        for item in items:

            asin = item.get_attribute("data-asin")
            if not asin:
                continue

            title_el = item.query_selector("h2 span")
            price_el = item.query_selector("span.a-price span.a-offscreen")
            rating_el = item.query_selector("span.a-icon-alt")

            if not title_el:
                continue

            title = title_el.inner_text().strip()
            price = price_el.inner_text() if price_el else "N/A"
            rating = rating_el.inner_text() if rating_el else "N/A"

            products.append({
                "title": title,
                "price": price,
                "rating": rating,
                "url": f"https://www.amazon.com/dp/{asin}"
            })

            if len(products) == 5:
                break


        browser.close()

    return products
