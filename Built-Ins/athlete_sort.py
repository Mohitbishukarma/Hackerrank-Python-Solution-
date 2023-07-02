n,m = list(map(int, input().split(" ")))
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]
k = int(input())
arr_sorted = sorted(arr, key= lambda x: x[k])
for i in arr_sorted: print(*i)