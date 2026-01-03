from multiprocessing import Process, Queue
import time

def server(request_queue, response_queue):
    print("[Server] Started. Waiting for requests...")
    while True:
        request = request_queue.get()
        if request == "STOP":
            print("[Server] Stopping.")
            break
        client_id, payload = request
        print(f"[Server] Received from Client-{client_id}: {payload}")

        # Simulate some "business logic"
        time.sleep(1)
        response = payload[::-1]  # Reverse the string as a dummy operation

        response_queue.put((client_id, response))
        print(f"[Server] Sent response to Client-{client_id}")
def client(client_id, request_queue, response_queue, message):
    print(f"[Client-{client_id}] Sending: {message}")
    request_queue.put((client_id, message))
    # Wait for response
    while True:
        resp_client_id, resp = response_queue.get()
        if resp_client_id == client_id:
            print(f"[Client-{client_id}] Got response: {resp}")
            break
        else:
            # If response is for another client, put it back
            response_queue.put((resp_client_id, resp))
if __name__ == "__main__":
    request_queue = Queue()
    response_queue = Queue()

    # Start server
    server_process = Process(target=server, args=(request_queue, response_queue))
    server_process.start()
    # Start clients
    messages = ["hello", "inter-process communication", "message queues"]
    clients = []
    for cid, msg in enumerate(messages):
        p = Process(target=client, args=(cid, request_queue, response_queue, msg))
        p.start()
        clients.append(p)
    # Wait for all clients
    for p in clients:
        p.join()
    # Tell server to stop
    request_queue.put("STOP")
    server_process.join()
    print("[Main] All processes finished.")
