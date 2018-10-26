from flask import (
    Flask,
    Response
)
import json
import time
import pika
import redis
import requests

from dto import User
app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

DATA_LOCATION_URL = "http://localhost:7000/v3/async/{user_id}/data"


@app.route("/v3/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = User()
    user.id = user_id
    # Send to the queue
    send_message(user)

    location = {
        'url': DATA_LOCATION_URL.format(user_id=user_id)
    }
    return Response(json.dumps(location), status=202, mimetype='application/json')


@app.route("/v3/async/users/<user_id>/data", methods=['GET'])
def get_user_data(user_id):
    user = redis_client.get('user_key_' + user_id)
    response = user.decode("utf-8") if user else {"status": "procesing"}
    return Response(response, status=200, mimetype='application/json')


def send_message(user):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='user_queue')
    channel.basic_publish(
        exchange='',
        routing_key='username_domain',
        body=json.dumps(user.__dict__),
    )
    connection.close()


if __name__ == '__main__':
    app.run(debug=True, port=7000)
