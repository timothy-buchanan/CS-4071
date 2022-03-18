# Left-to-Right Binary method finds the decimal representation of a binary number in an efficient way
# Lines 7 to 9
#


def LefttoRight(binaryN):
    numDigits = len(binaryN)
    power = 1
    for i in range(1, numDigits):
        power = power * 2  # Doubling power is equivalent of squaring it
        if binaryN[i] == '1':
            power = power + 1
        # print(str(power)) shows the powers after 1
    return power


def binaryRep(n):  # finds the binary representation of n
    if n == 0:
        return ""
    if n % 2 == 0:
        return binaryRep(n / 2) + "0"
    else:
        n = n - 1
        return binaryRep(n / 2) + "1"


n = int(input("Input a number "))
binaryN = binaryRep(n)
print(str(binaryN) + " is the binary representation of " + str(n))
nRecalculated = LefttoRight(binaryRep(n))
print("Putting " + str(binaryN) + " through the left-to-right binary method results in " + str(nRecalculated))
