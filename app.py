from flask import Flask, render_template, json, jsonify, request,redirect, url_for
import os

from Parser.Parser import Parser

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app_config = os.path.join(SITE_ROOT, "config", 'app_config.json')

with open(app_config) as f:
    config = json.load(f)

app = Flask(__name__)
key=''

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/articles/show')
def show_article():
    article_url= request.args.get('url')
    parser = Parser(article_url)
    return parser.get_fullText()


if __name__ == "__main__":
    app.run(debug=config['debug'], port=config['port'])