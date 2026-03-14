from services.keyword_service import generate_keywords
from services.cluster_service import build_clusters
from services.amazon_scraper_service import scrape_products
from services.amazon_affiliate_service import add_affiliate
from services.ai_article_service import generate_article
from services.wordpress_service import publish
from templates.pillar_template import render_pillar

def run(seed):

    keywords = generate_keywords(seed)

    clusters = build_clusters(keywords)

    for cluster in clusters:

        products = scrape_products(cluster)

        products = add_affiliate(products)

        pillar_text = generate_article(cluster, "pillar")

        pillar = render_pillar(pillar_text, products)

        publish(cluster, pillar)

        for kw in clusters[cluster]:

            article = generate_article(kw, "support")

            publish(kw, article)
