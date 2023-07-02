n, nums = input(), list(map( int ,input().split(" ")))
isAllPositive = all( [ i>0 for i in nums])
isPD = any([ str(i)[::-1] == str(i) for i in nums]) if isAllPositive else False
print(True if isAllPositive and isPD else False)
