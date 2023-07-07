n,m =input().split(' ')
pattern = '.|.'
for i in range(int(n)//2):
    print((pattern*(2*(i+1)-1)).center(int(m),'-'))
print("WELCOME".center(int(m),'-'))
for i in range(int(n)//2):
    print((pattern*(2*((int(n)//2)-i)-1)).center(int(m),'-'))
