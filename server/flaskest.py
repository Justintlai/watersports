import flask_cors
from flask import Flask
from flask import json
from flask import request

from newscraper import get_articles

app = Flask(__name__)
flask_cors.CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    topic = request.form['topic']
    print(topic)
    skipNum = request.form['skipNum']
    print(skipNum)

    data = get_articles(topic, skipNum)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
