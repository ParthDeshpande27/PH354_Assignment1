# Exercise 9: The semi-empirical mass formula

import math

# Part A
def BEcalc(Z, A):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    if A % 2 != 0:
        a5 = 0
    elif A % 2 == 0 and Z % 2 == 0:
        a5 = 12.0
    elif A % 2 == 0 and Z % 2 != 0:
        a5 = -12.0

    B = a1*A - a2*A**(2/3) - a3*(Z**2/A**(1/3)) - a4*((A - 2*Z)**2/A) +(a5/A**(1/2))
    return B

Z = int(input("Enter the atomic number Z: "))
A = int(input("Enter the mass number A: "))

print("For input Z and A, Binding Energy is as following:")
print(BEcalc(Z,A))

print("For Z=28, A=58, Binding Energy is as following:")
print(BEcalc(28,58))

# Part B
def BperNcalc(Z, A):
    BperN = BEcalc(Z, A)/A
    return BperN

print("For input Z and A, Binding Energy per nucleon is as following:")
print(BperNcalc(Z,A))

print("For Z=28, A=58, Binding Energy per nucleon is as following:")
print(BperNcalc(28,58))

# Part C
def StableforZ(Z):
    BperNmax = 0
    Buffer = 0
    bufferidx = Z
    for idx in range(Z, 3*Z):
        Buffer = BperNcalc(Z, idx)
        if Buffer > BperNmax:
            BperNmax = Buffer
            bufferidx = idx
    return BperNcalc(Z, bufferidx), Z, bufferidx, BEcalc(Z, bufferidx)

print("BperN, Input Z, most stable A, BE is as following:")
print(StableforZ(Z))

# Part D
result = [[]]*100
for idx in range(1, 101):
    result[idx-1] = list(StableforZ(idx))
    print(result[idx-1])

print("The state corresponding to the highest binding energy per nucleon is given below:")
print(max(result[:][:]))

