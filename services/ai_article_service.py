import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_article(keyword, article_type):

    prompt = f"""
Write a SEO optimized article.

Keyword: {keyword}
Type: {article_type}

1200 words
Use headings H2 H3
Include product recommendations
"""

    response = openai.ChatCompletion.create(

        model="gpt-4",

        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]
