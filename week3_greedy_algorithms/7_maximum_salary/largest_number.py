#Problem Introduction#
#Problem Introduction
#As the last question of a successful interview, your boss gives you a few pieces of paper with numbers on it and asks you to compose a largest number from these numbers. The resulting number is going to be your salary, so you are very much interested in maximizing this number. How can you do this?

#Problem Description#
#Input Format: The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.
#Task: Compose the largest number out of a set of integers.
#Constraints: 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 103 for all 1 ≤ 𝑖 ≤ 𝑛.
#Output Format: Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.




#Uses python3

import sys

def larger_number(n,m):
    if n+m >= m+n : return n
    else: return m
            
def largest_number(a):
    res = ""
    while len(a) > 1:
        max_ = a[0]
        for y in a[1:]: 
            max_ = larger_number(max_,y)
        res += max_
        a.remove(max_)
    res += a[0]
    return res

if __name__ == '__main__':
    n = int(input())
    a = list(input().split())
    print(int(largest_number(a)))