#Problem Description#
#Task: Find the first occurence of an integer in the given sorted sequence of integers (possibly with duplicates).
#Input Format: The first two lines of the input contain an integer 𝑛 and a sequence 𝑎0 ≤ 𝑎1 ≤ · · · ≤ 𝑎𝑛−1 of 𝑛 positive integers in non-decreasing order. The next two lines contain an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
#Constraints: 1 ≤ 𝑘 ≤ 105; 1 ≤ 𝑛 ≤ 3 · 104; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 109 for all 0 ≤ 𝑗 < 𝑘;
#Output Format: For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 of the first occurrence of 𝑏𝑖 (i.e., 𝑎𝑗 = 𝑏𝑖) or −1 if there is no such index.


def binary_search_first_instance(keys, query):
    low = 0
    high = len(keys)-1
    mid = low+((high-low)//2)
    while low <= high:
        if (query == keys[mid]) and (mid == 0 or query > keys[mid - 1]):
            return mid
        if query > keys[mid]:
            low = mid + 1
            mid = low + ((high-low)//2)
        else:
            high = mid - 1
            mid = low + ((high-low)//2)
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search_first_instance(input_keys, q), end=' ')
