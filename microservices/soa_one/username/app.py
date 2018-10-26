import time
from flask import (
  Flask,
  jsonify
)
app = Flask(__name__)


@app.route("/v2/username/<int:user_id>", methods=['GET'])
def get_username(user_id):
    return 'ariel' if user_id == 1 else 'pepe'


if __name__ == '__main__':
    app.run(debug=True, port=6001)
