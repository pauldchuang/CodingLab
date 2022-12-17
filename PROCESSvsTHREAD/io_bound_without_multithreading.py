import time
import requests

def io_bound_request_worker():            
    requests.get("https://api.my-ip.io/ip")

def main():    
    start_time = time.time()        

    for _ in range(100):
        io_bound_request_worker()
        
    print(f"Total time spent: {time.time() - start_time} seconds.")

if __name__ == '__main__':
    main()