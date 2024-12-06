import requests
import os


def search_web(query):
    api_key = 'AIzaSyBf719x1yQKQKmy1v0yuFOsXWWpG2vPf7c'
    cse_id = '3707af7df34764449'

    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cse_id}&q={query}"

    response = requests.get(url)
    results = response.json()

    if 'items' in results:
        return [item['link'] for item in results['items']]
    else:
        return []