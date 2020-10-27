import concurrent.futures
from concurrent.futures import ProcessPoolExecutor


check = {'a':1}


def p1(check):
    b = 2
    return b

def p2(check):
    c = 3
    return c

def p3(check):
    d = 4
    return d

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        r1 = executor.submit(p1 , check )
        r2 = executor.submit(p2 , check)
        r3 = executor.submit(p3 , check)
        check['b'] = r1.result() 
        check['c'] = r2.result() 
        check['d'] = r3.result() 
        
    
    return check

if __name__ == '__main__':
    val = main()
    
    print(val)