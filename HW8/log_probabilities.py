#范權榮 111210557
import math

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
p = 0.5
n = 10000


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------
def log_pow(p, n, base='e'):
    """Compute log_base(p^n) using the identity n*log_base(p)."""
    if base in ('e', 'ln', None):
        return n * math.log(p)
    elif base == 10:
        return n * math.log10(p)
    elif base == 2:
        return n * math.log2(p)
    else:
        return n * math.log(p) / math.log(base)


def scientific_notation_from_log10(log10_val):
    """Convert a log10 value into scientific notation (mantissa × 10^exponent)."""
    exponent = math.floor(log10_val)
    fractional = log10_val - exponent
    mantissa = 10 ** fractional
    return mantissa, exponent


def log_sum_exp(a, b):
    """
    Compute log(e^a + e^b) using the log-sum-exp trick.
    Prevents overflow when a or b are very large.
    """
    m = max(a, b)
    return m + math.log(math.exp(a - m) + math.exp(b - m))


# ------------------------------------------------------------
# Direct computation (WILL underflow)
# ------------------------------------------------------------
direct = p ** n  # expected to be 0.0

# ------------------------------------------------------------
# Logarithmic computations
# ------------------------------------------------------------
ln_val = log_pow(p, n, 'e')
log10_val = log_pow(p, n, 10)
log2_val = log_pow(p, n, 2)

mantissa, exponent = scientific_notation_from_log10(log10_val)

# ------------------------------------------------------------
# Demo log-sum-exp
# ------------------------------------------------------------
a = -5000
b = -7000
lse = log_sum_exp(a, b)

# ------------------------------------------------------------
# Print results
# ------------------------------------------------------------
print("--------------------------------------------------")
print("Direct computation:")
print("0.5**10000 =", direct)
print()

print("--------------------------------------------------")
print("Logarithmic computation using log(p^n) = n log(p):")
print("Natural log (ln):       ", ln_val)
print("Base-10 log (log10):    ", log10_val)
print("Base-2 log (log2):      ", log2_val)
print()

print("--------------------------------------------------")
print("Scientific notation from log10:")
print(f"0.5**10000 ≈ {mantissa} × 10^{exponent}")
print()

print("--------------------------------------------------")
print("log_pow() helper examples:")
print("log_pow(0.5, 10000, 'e')  =", ln_val)
print("log_pow(0.5, 10000, 10)   =", log10_val)
print("log_pow(0.5, 10000, 2)    =", log2_val)
print()

print("--------------------------------------------------")
print("Log-Sum-Exp example:")
print("Given a =", a, "and b =", b)
print("Naive log(exp(a)+exp(b)) would underflow!")
print("But log_sum_exp(a,b) gives:", lse)
print("--------------------------------------------------")
