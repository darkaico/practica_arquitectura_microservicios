from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Un cambio aca!"


"""
@api {get} /hola/<nombre> Saludar al usuario

@apiParam {nombre} Nombre del usuario
"""
@app.route("/hola/<nombre>")
def hello_name():
    return "Hola !" + nombre


if __name__ == '__main__':
    app.run(debug=True)
