import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    r = y / ppy
    t = np.arange(1, n + 1)

    coupon = face * couponRate / ppy
    cf = np.full(n, coupon, dtype=float)
    cf[-1] += face

    pv = (1 + r) ** (-t)
    pvcf = cf * pv

    duration_periods = np.sum(t * pvcf) / np.sum(pvcf)
    duration_years = duration_periods / ppy

    return duration_years
