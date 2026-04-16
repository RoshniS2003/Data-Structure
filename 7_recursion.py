# Recursion Using Stack

def factorial(n):
    # print("Function call: factorial(",n,")")

    if n==0 or n==1:
        return 1
    
    return n*factorial(n-1)

num = 5
result = factorial(num)
print("Result:",result)