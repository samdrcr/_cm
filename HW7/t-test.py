#范權榮 111210557
import math
from scipy.stats import t

def t_test_1sample(sample, mu0):
    n = len(sample)
    xbar = sum(sample) / n
    s = math.sqrt(sum((x - xbar)**2 for x in sample) / (n - 1))

    t_stat = (xbar - mu0) / (s / math.sqrt(n))
    df = n - 1
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    return t_stat, df, p_value
#范權榮 111210557
