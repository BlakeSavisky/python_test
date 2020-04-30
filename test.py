import math

def isprime(n):
    if (n < 2): 
        return False
    for i in range(2,math.ceil(math.sqrt(n))):
        print(i)
        if (n % i == 0):
            return False
    return True

print(isprime(35)) 
print("jesus")
print("hello world")