#Problem Introduction#
#A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.

#Problem Description#
#Task: The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
#Input Format: The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack. The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively. 
#Constraints: 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106; 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.
#Output Format: Output the maximal value of fractions of items that fit into the knapsack. The absolute value of the difference between the answer of your program and the optimal value should be at most 10−3. To ensure this, output your answer with at least four digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding issues)




# Uses python3
import sys

def get_optimal_value(capacity, items):
    V = 0
    W = 1   
    value = 0    
    items.sort(key=lambda x: x[V]/x[W], reverse=True)
    
    for item in items:
        if capacity <= 0:
            break    
    
        if item[W] > capacity:
            value += capacity * (item[V]/item[W])
            capacity = 0
                    
        elif item[W] <= capacity:
            value += item[V]
            capacity -= item[W]        
        
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    items = []
    for i in range(n):
        items.append(list(map(int, input().split())))
        
    opt_value = get_optimal_value(capacity, items)
    print("{:.4f}".format(round(opt_value, 4)))