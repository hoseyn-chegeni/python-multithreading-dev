import threading
import time


def sleeper(n, name):
    print(f'Hi, i am {name} and im going to sleep for {n} second')
    time.sleep(n)
    print(f'{name} has woken up from sleep')


t = threading.Thread(target= sleeper, name= 'sleeper', args=(5, 'thread1'))
t.start()
t.join()   # Blocking Method.
print('this is test.')