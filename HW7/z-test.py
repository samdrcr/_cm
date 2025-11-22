#范權榮 111210557
import math
from scipy.stats import norm

def z_test_1sample(sample, mu0, sigma):
    n = len(sample)
    xbar = sum(sample) / n
    z = (xbar - mu0) / (sigma / math.sqrt(n))

    # two-tailed p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))
    return z, p_value
#范權榮 111210557
