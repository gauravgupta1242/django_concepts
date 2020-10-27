from multiprocessing import Process
import time


def do_something(time_for_sleep):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
 


start = time.perf_counter()








# p1 = Process(target=do_something, args=[10])
# p2 = Process(target=do_something, args=[10])



if __name__ == '__main__':
    processes = []
    for _ in range(10):
        p = Process(target=do_something, args=[5])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    finish = time.perf_counter()
    print('\n')
    print(f'Finished in {round(finish-start,2 )} second(s)')
    print('\n')
    print('Ideally this process would take 10 seconds to run it Syncronously.')