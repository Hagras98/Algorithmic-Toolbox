#Problem Introduction#
#In this problem, you will design and implement an elementary greedy algorithm used by cashiers all over the world millions of times per day.

#Problem Description#
#Task: The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.
#Input Format: The input consists of a single integer 𝑚.
#Constraints: 1 ≤ 𝑚 ≤ 103.
#Output Format: Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.




# Uses python3
import sys


def get_change(m):
    n_coins = m // 10
    m %= 10
    if m >= 5:
        n_coins += 1
        m -= 5
    n_coins += m
    return n_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
