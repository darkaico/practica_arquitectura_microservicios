import time
from flask import (
  Flask,
  jsonify
)
app = Flask(__name__)


@app.route("/monolithic/users/<user_id>", methods=['GET'])
def get_user(user_id):
    user = {
      'username': UsernameService().process(user_id),
      'name': NameService().process(user_id),
      'twitter': TwitterService().process(user_id)
    }

    return jsonify(user)


class UsernameService:

  def process(self, user_id):
    return 'ariel' if user_id == 1 else 'pepe'


class NameService:

  def process(self, user_id):
    return 'Ariel Parra' if user_id == 1 else 'Pepe Argento'


class TwitterService:

  def process(self, user_id):
    time.sleep(0.5)
    return '@darkaico' if user_id == 1 else '@pepeargento'


if __name__ == '__main__':
    app.run(debug=True)
