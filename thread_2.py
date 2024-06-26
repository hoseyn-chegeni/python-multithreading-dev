import threading
import time

def sleeper(n, name):
    print(f'Hi, I am {name}')
    time.sleep(n)
    print(f'{name} has woken up from sleep')

threads_list = []
start = time.time()

for i in range(5):
    t = threading.Thread(target=sleeper,name = f'thread-{i}', args=(5, f'thread-{i}'))
    threads_list.append(t)
    t.start()

for i in threads_list:
    t.join()

print('all five thread have finished thier job')

end = time.time()


print(f'time taken: {start}-{end}')