from config.settings import AMAZON_AFFILIATE_TAG

def add_affiliate(products):

    for p in products:

        if "?" in p["url"]:
            p["url"] += f"&tag={AMAZON_AFFILIATE_TAG}"
        else:
            p["url"] += f"?tag={AMAZON_AFFILIATE_TAG}"

    return products
