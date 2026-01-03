from multiprocessing import Process, Pipe

def child_process(conn):
    print("[Child] Waiting for message...")
    
    # receive from parent
    msg = conn.recv()
    print("[Child] Received:", msg)

    # send reply
    reply = msg.upper() + " (from child)"
    conn.send(reply)
if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    # start child process
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    # parent sends a message
    parent_conn.send("hello child")
    print("[Parent] Sent: hello child")

    # parent receives reply
    print("[Parent] Received:", parent_conn.recv())
    p.join()
