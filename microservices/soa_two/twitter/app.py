import json
import pika
import redis
import time

from dto import User

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


class TwitterService:

    def start(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='twitter_domain')
        channel.basic_consume(
            self.process,
            queue='twitter_domain',
            no_ack=True,
        )
        channel.start_consuming()

    def process(self, ch, method, properties, body):
        time.sleep(0.5)
        user = json.loads(body)
        user['twitter'] = '@darkaico' if user['id'] == 1 else '@pepeargento'
        self.save_user(user)

    def save_user(self, user):
        user = redis_client.set('user_key_' + str(user['id']), user)


if __name__ == '__main__':
    TwitterService().start()
