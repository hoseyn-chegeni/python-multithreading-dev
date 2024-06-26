import threading
import time

def sleeper(n, name):
    print(f'Hi, I am {name}')
    time.sleep(n)
    print(f'{name} has woken up from sleep')

# Create a Thread object and start the thread
t = threading.Thread(target=sleeper, args=(5, 'sepdie'))

t.start()
t.join() # Blocking method 

print('hello')