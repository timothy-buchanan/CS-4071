# Finds the greatest common denominator through Euclid GCD

a = int(input("What is the first number(a)?"))
b = int(input("What is the first number(b)?"))

while b != 0:
    r = a % b
    a = b
    b = r

print("GCD is " + str(a))
