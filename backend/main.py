from flask import Flask, request, jsonify
from search_engine import search_web
from web_scraper import scrape_content
from content_processor import process_content

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']

    # Search for relevant websites
    search_results = search_web(query)

    # Scrape content from the first result
    if search_results:
        content = scrape_content(search_results[0])

        # Process and summarize the content
        result = process_content(content, query)

        return jsonify({'result': result})
    else:
        return jsonify({'result': 'No results found'})


if __name__ == '__main__':
    app.run(debug=True)