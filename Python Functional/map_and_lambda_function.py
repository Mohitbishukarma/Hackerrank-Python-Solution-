cube = lambda x: x**3

def fibonacci(n):
    fib_gen = lambda x: 0 if x == 1 else 1 if x == 2 else fib_gen(x-1)+fib_gen(x-2)
    return [fib_gen(x) for x in range(1,n+1)]
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))