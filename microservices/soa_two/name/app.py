import json
import pika
import time

from dto import User


class NameService:

    def start(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='name_domain')
        channel.basic_consume(
            self.process,
            queue='name_domain',
            no_ack=True,
        )
        channel.start_consuming()

    def process(self, ch, method, properties, body):
        user = json.loads(body)
        user['name'] = 'Ariel Parra' if user['id'] == 1 else 'Pepe Argento'

        self.send_message(user)


    def send_message(self, user):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='twitter_domain')
        channel.basic_publish(
            exchange='',
            routing_key='twitter_domain',
            body=json.dumps(user),
        )
        connection.close()


if __name__ == '__main__':
    NameService().start()
