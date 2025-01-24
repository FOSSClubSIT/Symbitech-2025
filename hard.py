# There's an issue with the final counter value not being correct.
# Hint: The problem here lies in how threads are accessing and modifying the counter variable.
import threading

counter = 0

# Function to increment the counter
def increment():
    global counter
    for _ in range(1000):
        counter += 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
