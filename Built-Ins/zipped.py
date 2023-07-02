n,x = list(map(int, input().split()))
marks = [list(map(float,input().split(" "))) for _ in range(x)]
marks = list(zip(*marks))
for each in marks: print(sum(each)/x)