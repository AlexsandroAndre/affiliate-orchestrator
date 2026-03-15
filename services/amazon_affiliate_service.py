from config.settings import AMAZON_AFFILIATE_TAG, REQUEST_DELAY
import time

def add_affiliate(products):    

    for p in products:
        time.sleep(REQUEST_DELAY)
        
        if "?" in p["url"]:
            p["url"] += f"&tag={AMAZON_AFFILIATE_TAG}"
        else:
            p["url"] += f"?tag={AMAZON_AFFILIATE_TAG}"

    return products
