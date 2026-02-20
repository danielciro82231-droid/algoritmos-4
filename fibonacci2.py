def Fibonacci(n):
    if n<=1:
        return n

    retturn Fibonacci(n-1) + Fibonacci(n-2)

def Fibonacci_tail(n, actual=0, siguiente=1):
    









import time
inicio = time.time()
print(Fibonacci(30))
print(time.time() - inicio)
