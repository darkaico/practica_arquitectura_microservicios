import time
import requests
from flask import (
  Flask,
  jsonify
)
app = Flask(__name__)

USERNAME_SERVICE_URL = 'http://127.0.0.1:6001/version_one/username/'
NAME_SERVICE_URL = 'http://127.0.0.1:6002/version_one/name/'
TWITTER_SERVICE_URL = 'http://127.0.0.1:6003/version_one/twitter/'


@app.route("/version_one/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = {
      'username': get_client_response(USERNAME_SERVICE_URL + user_id),
      'name': get_client_response(NAME_SERVICE_URL + user_id),
      'twitter': get_client_response(TWITTER_SERVICE_URL + user_id)
    }

    return jsonify(user)

def get_client_response(url):
  return requests.get(url).text


if __name__ == '__main__':
    app.run(debug=True, port=6000)
