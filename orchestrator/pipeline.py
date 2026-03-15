from services.keyword_service import generate_keywords
from services.cluster_service import build_clusters
from services.amazon_scraper_service import  scrape_amazon_products
from services.amazon_affiliate_service import add_affiliate
from services.ai_article_service import generate_article
from services.wordpress_service import publish
from templates.pillar_template import render_pillar

def run(seeds, post_limit):

    count = 0

    for seed in seeds:

        keywords = generate_keywords(seed)

        clusters = build_clusters(keywords)

        for cluster in clusters:

            if count >= post_limit:
                return

            products = scrape_amazon_products(cluster)

            products = add_affiliate(products)

            pillar_text = generate_article(cluster, "pillar")

            pillar = render_pillar(pillar_text, products)

            publish(cluster, pillar)

            count += 1

            for kw in clusters[cluster]:

                if count >= post_limit:
                    return

                article = generate_article(kw, "support")

                publish(kw, article)

                count += 1
