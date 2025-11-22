#范權榮 111210557
def t_test_2sample_unequal_var(sample1, sample2):
    n1, n2 = len(sample1), len(sample2)
    x1, x2 = sum(sample1)/n1, sum(sample2)/n2

    s1 = sum((x - x1)**2 for x in sample1) / (n1 - 1)
    s2 = sum((x - x2)**2 for x in sample2) / (n2 - 1)

    t_stat = (x1 - x2) / math.sqrt(s1/n1 + s2/n2)

    # Welch-Satterthwaite degrees of freedom
    df = (s1/n1 + s2/n2)**2 / ((s1**2)/(n1**2*(n1-1)) + (s2**2)/(n2**2*(n2-1)))

    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    return t_stat, df, p_value
