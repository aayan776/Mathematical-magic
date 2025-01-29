import math
#Check prime
number = int(input("Enter number: "))
if number > 1:
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
#Find prime
def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p] == True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num + 1):
        if prime[p]:
            print(p)
num = int(input("Enter number: "))
print("\n")
print(f"Every prime number less than or equal to {num}:")
SieveOfEratosthenes(num)
#Prime palindromes
a = 3000
print("\n")
print("All palindrome prime numbers:")
for numb in range(1, a + 1):
    c = 0
    rev = 0
    temp = numb
    for i in range(1, temp + 1):
        if temp % i == 0:
            c += 1
    if c == 2:
        while temp > 0:
            rev = rev * 10 + (temp % 10)
            temp //= 10
        if rev == numb:
            print(numb)