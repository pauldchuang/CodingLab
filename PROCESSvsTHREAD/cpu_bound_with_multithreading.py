from concurrent.futures import ThreadPoolExecutor, wait
import time

def cpu_bound_factorial(n): 
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main():    
    start_time = time.time()          
    elements = [100000 + x for x in range(10)]    
     
    with ThreadPoolExecutor(max_workers=5) as executor:
        threads = []
        for ele in elements:   
            t = executor.submit(cpu_bound_factorial, ele)
            threads.append(t)                            
        wait(threads)        
                
    print(f"Total time spent: {time.time() - start_time} seconds.")

if __name__ == '__main__':
    main()