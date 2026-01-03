import threading
import queue
import time
import random
class Broker:
    def __init__(self):
        # topic -> list of subscriber queues
        self.subscribers = {}
        self.lock = threading.Lock()
    def subscribe(self, topic, subscriber_queue):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []
            self.subscribers[topic].append(subscriber_queue)
            print(f"[Broker] New subscription on topic '{topic}'")
    def publish(self, topic, message):
        with self.lock:
            queues = self.subscribers.get(topic, [])
        print(f"[Broker] Publishing on '{topic}': {message} to {len(queues)} subscriber(s)")
        for q in queues:
            q.put((topic, message))
def subscriber(name, broker, topic):
    q = queue.Queue()
    broker.subscribe(topic, q)
    while True:
        topic, message = q.get()
        if message == "STOP":
            print(f"[Subscriber-{name}] Stopping.")
            break
        print(f"[Subscriber-{name}] Received on '{topic}': {message}")
def publisher(name, broker, topic, messages):
    for msg in messages:
        full_msg = f"{name} says: {msg}"
        broker.publish(topic, full_msg)
        time.sleep(random.uniform(0.5, 1.5))
    # Send STOP to indicate end of stream (optional)
    broker.publish(topic, "STOP")
if __name__ == "__main__":
    broker = Broker()
    # Subscriber threads
    sub1 = threading.Thread(target=subscriber, args=("A", broker, "sports"))
    sub2 = threading.Thread(target=subscriber, args=("B", broker, "news"))
    sub3 = threading.Thread(target=subscriber, args=("C", broker, "sports"))
    sub1.start()
    sub2.start()
    sub3.start()
    # Publisher threads
    pub1_messages = ["Team X won!", "Big match tomorrow.", "New player signed."]
    pub2_messages = ["Elections coming soon.", "New policy announced.", "Stock market rising."]
    pub1 = threading.Thread(target=publisher, args=("SportsPublisher", broker, "sports", pub1_messages))
    pub2 = threading.Thread(target=publisher, args=("NewsPublisher", broker, "news", pub2_messages))
    pub1.start()
    pub2.start()
    pub1.join()
    pub2.join()
    # Give some time for subscribers to consume STOP
    time.sleep(2)
    print("[Main] Ending program. Note: subscriber threads may still be running if STOP not handled for all topics.")
