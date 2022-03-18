# Better version of the power function
# Halves the exponent each iteration of the Power function
# Making it do about 2*log2(p) or 2p multiplications


def Power(x, p):
    if p == 1:
        return x
    if p % 2 == 0:
        return Power(x*x, p/2)
    else:
        return x*(Power(x*x,(p-1)/2))
