import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)

    out = np.array(nums, dtype=object)
    out[:] = nums.astype(str)

    m15 = (nums % 15 == 0)
    m3 = (nums % 3 == 0) & ~m15
    m5 = (nums % 5 == 0) & ~m15

    out[m3] = "fizz"
    out[m5] = "buzz"
    out[m15] = "fizzbuzz"
    return out.tolist()
