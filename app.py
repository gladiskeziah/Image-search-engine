from flask import Flask, render_template, request
import requests

app = Flask(__name__)


API_KEY = "AIzaSyAGW_LfPSumqIK9HS2_lDxcI_ALfuJhGY0"
SEARCH_ENGINE_ID = "b23e9fc0eb6c94bdd"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType=image"
        response = requests.get(url)
        results = response.json()

        if 'items' in results:
            return render_template('index.html', results=results['items'])
        else:
            return render_template('index.html', results=[])

    return render_template('index.html', results=[])

if __name__ == '__main__':
    app.run(debug=True)
