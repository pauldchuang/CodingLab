import time
from multiprocessing import Process
import requests

def io_bound_request_worker():                     
    requests.get("https://api.my-ip.io/ip")

def main():
    start_time = time.time()               
    procs = []

    for _ in range(100):
        proc = Process(target=io_bound_request_worker)
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()
    
    print(f"Total time spent: {time.time() - start_time} seconds.")

if __name__ == '__main__':
    main()    