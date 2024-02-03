# counter-incrementer-service.py
import time

counter = 0

while counter<60:
    counter += 1
    print(f"Counter: {counter}")
    time.sleep(60)  # Sleep for 1 minute
 