import math

def print_formatted(number):
    max_length = math.floor(math.log(number, 2)) + 1

    for i in range(1, number+1):
        d = str(i).rjust(max_length)
        o = str(oct(i))[2:].rjust(max_length)
        h = str(hex(i))[2:].upper().rjust(max_length)
        b = bin(i)[2:].lstrip('0').rjust(max_length)
        print('{} {} {} {}'.format(d,o,h,b))