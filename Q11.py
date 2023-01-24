# Exercise 11: Prime numbers

import math

# Part A
def binomial(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

print("A few examples of calculations using binomial(n,k):")
print("binomial(10,0):")
print(binomial(10,0))
print("binomial(6,4)")
print(binomial(6,4))
print("binomial(40, 3)")
print(binomial(40, 3))
print("binomial(20, 10)")
print(binomial(20, 10))

# Part B
print("\nFollow the first 20+1 lines of Pascal's triangle")
for i in range(0,21):
    for j in range(0,i+1):
        print(binomial(i,j), end=" ")
    print("")

# Part C

    # Subpart A
print("\nThe total probability that a coin tossed 100 times comes up heads exactly 60 times: ")
print(binomial(100, 60)/(2**100))

    # Subpart B
answer = 0
for i in range(60, 101):
    answer += binomial(100, i)
answer = answer/(2**100)
print("\nThe total probability that a coin tossed 100 times comes up heads 60 or more times: ")
print(answer)

    

