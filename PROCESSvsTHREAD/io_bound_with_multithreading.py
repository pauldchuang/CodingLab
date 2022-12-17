import time
from concurrent.futures import ThreadPoolExecutor, wait
import requests

def io_bound_request_worker():                     
    requests.get("https://api.my-ip.io/ip")    

def main():    
    start_time = time.time()        

    with ThreadPoolExecutor(max_workers=100) as executor:
        threads = []
        for _ in range(100):
            t = executor.submit(io_bound_request_worker)
            threads.append(t)                            
        wait(threads)        
                
    print(f"Total time spent: {time.time() - start_time} seconds.")

if __name__ == '__main__':
    main()