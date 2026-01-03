zeromq_subscriber.py:

import zmq
context = zmq.Context()
socket = context.socket(zmq.SUB)
# connect to publisher
socket.connect("tcp://127.0.0.1:5555")
# subscribe to all messages
socket.setsockopt_string(zmq.SUBSCRIBE, "")
print("Subscriber ready...")
while True:
    message = socket.recv_string()
    print("Received:", message)
____________________
zeromq_publisher.py

import zmq
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)
# bind to a port so subscribers can connect
socket.bind("tcp://127.0.0.1:5555")
messages = ["Hello", "ZeroMQ Pub-Sub Example", "Bye"]
while True:
    for msg in messages:
        print("Sending:", msg)
        socket.send_string(msg)
        time.sleep(1)
