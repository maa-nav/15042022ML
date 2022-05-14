import threading
import time
##
##x = 2
##
##lock = threading.Lock()
##
##def func1():
##    global x, lock
##    lock.acquire()
##    while x<500:
##        x*=2
##        print(x)
##        time.sleep(1)
##    print('func1 complete')
##    lock.release()
##
##def func2():
##    global x,lock
##    lock.acquire()
##    while x>1:
##        x/=2
##        print(x)
##        time.sleep(1)
##    print('func2 complete')
##    lock.release()
##
##t1 = threading.Thread(target = func1)
##t2 = threading.Thread(target = func2)
##
##t1.start()
##t2.start()
##t1.join()
##t2.join()

##$$$$$$$$$$$$$$$$$$ SEMAPHORE $$$$$$$$$$$$$$$$$$$$$$$$

start = time.perf_counter()

semaphore = threading.BoundedSemaphore(value=3)

def func(n):
    print(f'{n} is trying to access')
    semaphore.acquire()
    print(f'{n} access granted')
    time.sleep(10)
    print(f'{n} is released')
    semaphore.release()

threads = []

for n in range(1,11):
    t = threading.Thread(target = func, args = (n,))
    threads.append(t)
    t.start()
##    time.sleep(1)

for i in threads:
    i.join()


finish = time.perf_counter()
print(f'{finish-start} seconds to complete')







    
