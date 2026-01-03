from multiprocessing import Process, Queue
import time
def worker(worker_id, task_queue):
    while True:
        task = task_queue.get()     # read task
        if task is None:            # stop signal
            print(f"Worker {worker_id} stopping.")
            break
        print(f"Worker {worker_id} got:", task)
        time.sleep(1)  # simulate work
if __name__ == "__main__":
    q = Queue()
    # Start 2 worker processes
    workers = []
    for i in range(2):
        p = Process(target=worker, args=(i, q))
        p.start()
        workers.append(p)
    # Add tasks
    for t in range(5):
        print("[Parent] Sending task", t)
        q.put(t)
    # Send stop signal to each worker
    for _ in workers:
        q.put(None)
    for p in workers:
        p.join()
    print("All workers finished.")
