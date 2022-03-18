# Naive method for Power
# Not fastest solution by significant amount
# Deceptively looks p-1 multiplications which would be good
# But a more meaningful input would be binary digits of p
# Making it 2^p multiplications. Very inefficient for high values of p


def NaivePower(x, p):
    power = x
    for i in range(p):
        power = power * x
    return power

