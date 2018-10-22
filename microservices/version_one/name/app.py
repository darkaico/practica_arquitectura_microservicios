import time
from flask import (
  Flask,
  jsonify
)
app = Flask(__name__)


@app.route("/version_one/name/<user_id>", methods=['GET'])
def get_name(user_id):
    return 'Ariel Parra' if user_id == 1 else 'Pepe Argento'


if __name__ == '__main__':
    app.run(debug=True, port=6002)
