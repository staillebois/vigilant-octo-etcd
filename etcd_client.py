from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Queue

import etcd3
import uuid
import time


def add_entry(etcd_, d_queue_: Queue):
    print('Adding entry')
    etcd_key = str(uuid.uuid1())

    etcd_.put(etcd_key, etcd_key)
    print(f'PUT {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')
    etcd_.put(etcd_key, etcd_key)
    print(f'PUT update {etcd_key}')
    d_queue_.put(etcd_key)
    d_queue_.task_done()


def remove_entry(etcd_, d_queue_: Queue):
    print('Removing entry')
    etcd_key = d_queue_.get(timeout=60)
    print(f'DELETE {etcd_key}')
    etcd_.delete(etcd_key)
    d_queue_.task_done()


if __name__ == '__main__':
    print('Start')
    etcd = etcd3.client()
    d_queue = Queue()
    executor = ThreadPoolExecutor(max_workers=10)
    start_time = time.time()
    print(f'Start time: {start_time}')
    t_end = start_time + 60 * 1  # start time + 1 minutes
    while time.time() < t_end:
        try:
            executor.submit(add_entry, etcd, d_queue)
            executor.submit(remove_entry, etcd, d_queue)
            time.sleep(1)
        except Exception as e:
            print(e)
            executor.shutdown()
    executor.shutdown()
    print('Shutdown')
