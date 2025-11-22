#范權榮 111210557
def t_test_paired(before, after):
    d = [b - a for b, a in zip(before, after)]
    return t_test_1sample(d, mu0=0)   # reuse the 1-sample t-test
