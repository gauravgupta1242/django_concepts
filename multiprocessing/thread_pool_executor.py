import concurrent.futures
import concurrent.futures 
import time
start = time.perf_counter()
check = {'a':1}


def p1(check):
    time.sleep(1)
    b = 2
    return b

def p2(check):
    time.sleep(1)
    c = 3
    return c

def p3(check):
    time.sleep(1)
    d = 4
    return d

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as executor:
    val_1 = executor.submit(p1, check)
    val_2 = executor.submit(p2, check)
    val_3 = executor.submit(p3, check)
    check['b'] = val_1.result()
    check['c'] = val_2.result()
    check['d'] = val_3.result()

    print(check)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')


