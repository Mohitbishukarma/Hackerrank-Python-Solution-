x,k = list(map(int, input().split(" ")))
p = input().replace('x',str(x))
value = eval(p)
if value == k: print(True)
else: print(False)