import requests
from config.settings import WORDPRESS_URL, WORDPRESS_USER, WORDPRESS_APP_PASSWORD

def publish(title, content):

    data = {
        "title": title,
        "content": content,
        "status": "pending"
    }

    requests.post(
        WORDPRESS_URL,
        json=data,
        auth=(WORDPRESS_USER, WORDPRESS_APP_PASSWORD)
    )
