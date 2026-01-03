 rabbitmq_subscriber.py:

import pika
# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
# Declare fanout exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# Create temporary queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
# Bind queue to exchange
channel.queue_bind(exchange='logs', queue=queue_name)
print("[*] Waiting for messages. To exit press CTRL+C")
# Callback function
def callback(ch, method, properties, body):
    print("[Subscriber] Received:", body.decode())
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)
channel.start_consuming()
____________________________
 rabbitmq_publisher.py:

import pika
import time
# Connect to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()
# Declare fanout exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
messages = [
    "Hello Subscribers!",
    "This is a RabbitMQ Pub-Sub Demo",
    "Final Broadcast Message!"
]
for msg in messages:
    channel.basic_publish(
        exchange='logs',
        routing_key='',
        body=msg
    )
    print("[Publisher] Sent:", msg)
    time.sleep(1)
connection.close()
