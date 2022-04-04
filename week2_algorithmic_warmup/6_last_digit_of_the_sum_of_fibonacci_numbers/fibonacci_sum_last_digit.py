# Uses python3
import sys

def calc_fib(n):
    if (n <= 1):
        return n
    minus1 = 1
    minus2 = 0
    for i in range(n-1):
        fib = minus1 + minus2
        minus2 = minus1
        minus1 = fib
        
    return fib

def fibonacci_sum(n):
    if n <= 1:
        return n
    fibs = [0, 1]
    i = 2
    while(True):
        fibs.append(calc_fib(i) % 10)
        if fibs[i] == 1 and fibs[i-1] == 0:
            break
        i += 1
    period = len(fibs) - 2
    _sum = 0
    for num in fibs[:n%period +1]:        
        _sum += num

    return _sum % 10

if __name__ == '__main__':
   
    n = int(input())
    print(fibonacci_sum(n))
