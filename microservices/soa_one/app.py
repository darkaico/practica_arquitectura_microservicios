from flask import (
  Flask,
  Response
)
import json
import time
import requests

from dto import User

app = Flask(__name__)

USERNAME_SERVICE_URL = 'http://127.0.0.1:6001/v2/username/'
NAME_SERVICE_URL = 'http://127.0.0.1:6002/v2/name/'
TWITTER_SERVICE_URL = 'http://127.0.0.1:6003/v2/twitter/'


@app.route("/v2/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = User()
    user.id = user_id
    user.username = get_client_response(USERNAME_SERVICE_URL, user_id)
    user.name = get_client_response(NAME_SERVICE_URL, user_id)
    user.twitter = get_client_response(TWITTER_SERVICE_URL, user_id)

    return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')


def get_client_response(url, user_id):
  return requests.get(url + user_id).text


if __name__ == '__main__':
    app.run(debug=True, port=6000)
