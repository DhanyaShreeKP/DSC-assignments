from collections import Counter

def glove(n,arr):
    n = Counter(arr)
    return sum(i//2 for i in n.values())

n = input()
arr = list(map(int,input().split()))
print(glove(n,arr))