import time

def cpu_bound_factorial(n): 
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
def main():
    start_time = time.time()   
    elements = [100000 + x for x in range(10)]

    for ele in elements:
        cpu_bound_factorial(ele)

    print(f"Total time spent: {time.time() - start_time} seconds.")

if __name__ == "__main__":
    main()    