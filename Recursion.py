###
def foo(x):
    ### base cases


    ### recursive cases

def factorial(n:int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

