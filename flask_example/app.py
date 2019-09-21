import json

from flask import (
  Flask,
  render_template,
  send_from_directory,
)

app = Flask(__name__, static_folder = 'templates')

@app.route('/')
def index():
    return send_from_directory('templates', "index.html")

@app.route('/<path:path>')
def hello(path):
    return send_from_directory('templates', path)



"""
@api {get} /customers/<id> Obtener Cliente
@apiName GetCustomer
@apiGroup Customer

@apiParam {id} id del cliente

@apiSuccess {String} id Id del cliente.
@apiSuccess {String} name Nombre del cliente.
"""
@app.route("/v1/customers/<id>")
def get_customer(id):
    return json.dumps({
        "id": id,
        "name": "Ariel"
    })

"""
@api {delete} /customers/<id> Elimina un Cliente
@apiName DeleteCustomer
@apiGroup Customer

@apiParam {id} id del cliente

@apiSuccess {Boolean} success Resultado de la operacion
"""
@app.route("/v1/customers/<id>", methods=['DELETE'])
def delete_customer(id):
    return json.dumps({
        "success": True
    })


if __name__ == '__main__':
    app.run(debug=True)
