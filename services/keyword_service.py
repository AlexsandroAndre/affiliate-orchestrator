import requests
import string

def google_suggest(keyword):

    url = "https://suggestqueries.google.com/complete/search"

    params = {
        "client": "firefox",
        "q": keyword
    }

    r = requests.get(url, params=params)

    return r.json()[1]

def generate_keywords(seed, limit=500):

    keywords = []

    keywords.extend(google_suggest(seed))

    for letter in string.ascii_lowercase:

        suggestions = google_suggest(f"{seed} {letter}")

        keywords.extend(suggestions)

    keywords = list(set(keywords))

    return keywords[:limit]
