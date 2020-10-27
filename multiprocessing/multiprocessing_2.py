from multiprocessing import Process
import time


start = time.perf_counter()


def process_1(val):
    time.sleep(1)
    a = val + 1
    
    return a 

def p1(val):
    print("process_1",process_1(1))

def p2(val):
    print("process_2",process_1(process_1(process_1(1))))

def p3(val):
    print("process_3",process_1(process_1(1)))


# p1(1)
# p2(1)
# p3(1)
# p1 = Process(target=do_something, args=[10])
# p2 = Process(target=do_something, args=[10])



if __name__ == '__main__':
    # processes = []
    # for _ in range(10):
    #     p = Process(target=do_something, args=[5])
    #     p.start()
    #     processes.append(p)
    # for process in processes:
    #     process.join()

    p11 = Process(target=p1,args=[1])
    p11.start()
    p12 = Process(target=p2,args=[1])
    p12.start()
    p13 = Process(target=p3,args=[1])
    p13.start()
    
    processes = [p11,p12,p13]
    for process in processes:
        process.join()
    finish = time.perf_counter()
    print('\n')
    print(f'Finished in {round(finish-start,2 )} second(s)')