# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    while true:
        if n - i > i + 1:
            summands.append(i)
            n -= i
            i += 1
        else:
            summands.append(n)
            break
    
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
