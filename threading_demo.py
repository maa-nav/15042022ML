import time
import threading
import concurrent.futures

start = time.perf_counter()


def func(seconds):     # argument seconds has pass after for thread loop
    print(f'Sleeping for {seconds} second...\n')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

##t1 = threading.Thread(target = func)
##t2 = threading.Thread(target = func)
##
##t1.start()
##t2.start()
##t1.join()
##t2.join()

##threads = []
##for _ in range(10):
##    t = threading.Thread(target = func)
##    t.start()
##    threads.append(t)
##
##for thread in threads:
##    thread.join()


with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit method - Schedule the function to be executed and returns a future object.
##    f1 = executor.submit(func,1)
##    f2 = executor.submit(func,1)
##    print(f1.result())
##    print(f1.result())


    secs = [5,4,3,2,1]

##    results = [executor.submit(func,i) for i in secs]
##    for i in concurrent.futures.as_completed(results):
##        print(i.result())

    results = executor.map(func,secs)
    for result in results:
        print(result)




    


finish = time.perf_counter()
print(f'Finshed in {round(finish - start),2} second')
