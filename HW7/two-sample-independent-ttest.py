#范權榮 111210557
def t_test_2sample_equal_var(sample1, sample2):
    n1, n2 = len(sample1), len(sample2)
    x1, x2 = sum(sample1)/n1, sum(sample2)/n2

    s1 = sum((x - x1)**2 for x in sample1)
    s2 = sum((x - x2)**2 for x in sample2)

    # pooled variance
    sp2 = (s1 + s2) / (n1 + n2 - 2)

    t_stat = (x1 - x2) / math.sqrt(sp2 * (1/n1 + 1/n2))
    df = n1 + n2 - 2
    p_value = 2 * (1 - t.cdf(abs(t_stat), df))
    return t_stat, df, p_value
