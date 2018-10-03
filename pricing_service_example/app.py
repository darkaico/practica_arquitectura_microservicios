from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "aca iria la documentacion"


@app.route("/pricing/<article_id>", methods=['GET'])
def get_article(article_id):
    return "article_id: " + article_id


@app.route("/pricing/<article_id>", methods=['POST'])
def update_article(article_id):
    return "Articulo actualizado con id: " + article_id


if __name__ == '__main__':
    app.run(debug=True)
