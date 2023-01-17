def s(n):
    if n == 0:
        return 1
    elif n == 1:
        return -4
    else:
        sn_2 = 1
        sn_1 = -4
        for i in range(2, n+1):
            sn = (-2*sn_1 - sn_2) % (10 ** 12)
            sn_2 = sn_1
            sn_1 = sn
        return sn

print(s(3))