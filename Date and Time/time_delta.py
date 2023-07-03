#!/bin/python3
import os
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    time_diff = t1 - t2
    return str(abs(int(time_diff.total_seconds())))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()