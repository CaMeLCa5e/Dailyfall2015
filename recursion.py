def factorial(n): 
    if n == 1: 
        return 1 
    else: 
        return n * factorial (n-1)

print factorial(5)        


def interactive_factorial (n): 
    result = 1 
    for i in range(2, n+1):
        result *= i 
    return result        

print interactive_factorial(5)    

def flatten_list(a, result=None):
    if result is None; 
        result = []
    for x in a: 
        if isinstance(x, list):
            flatten_list(x, result)
        else: 
            result.append(x)
    return result


def fib(n):
    if n is 0 or is 1: 
        return 1
    else:
        return fib(n-1) + fib(n-2)
        