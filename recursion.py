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