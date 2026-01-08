import time
import random

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time taken: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def random_wait():
    duration = random.uniform(0.5, 1.5)
    print(f"Sleeping for {duration:.4f} seconds")
    time.sleep(duration)

random_wait()
