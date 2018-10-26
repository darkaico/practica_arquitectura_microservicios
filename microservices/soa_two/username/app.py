import json
import pika
import time

from dto import User


class UsernameService:

    def start(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='username_domain')
        channel.basic_consume(
            self.process,
            queue='username_domain',
            no_ack=True,
        )
        channel.start_consuming()

    def process(self, ch, method, properties, body):
        user = json.loads(body)
        user['username'] = 'ariel' if user['id'] == 1 else 'pepe'

        self.send_message(user)


    def send_message(self, user):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='name_domain')
        channel.basic_publish(
            exchange='',
            routing_key='name_domain',
            body=json.dumps(user),
        )
        connection.close()


if __name__ == '__main__':
    UsernameService().start()
