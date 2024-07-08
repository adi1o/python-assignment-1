#File1(fact.py)

def fact(n):
    x = 1
    for i in range (1, n+1):
        x = x * i 
    return x
        
#File 2(question8.py)

from fact import fact 
n = int(input("Enter the number :"))
result = fact(n)
print("Factorial of your number is :",result)
