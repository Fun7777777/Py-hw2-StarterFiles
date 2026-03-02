import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    cf = np.full(n, coupon, dtype=float)
    cf[-1] += face

    pv = (1 + r) ** (-t)
    price = np.sum(cf * pv)

    return price
