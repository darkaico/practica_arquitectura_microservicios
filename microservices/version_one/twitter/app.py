import time
from flask import (
  Flask,
  jsonify
)
app = Flask(__name__)


@app.route("/version_one/twitter/<user_id>", methods=['GET'])
def get_twitter(user_id):
    time.sleep(0.5)
    return '@darkaico' if user_id == 1 else '@pepeargento'


if __name__ == '__main__':
    app.run(debug=True, port=6003)
