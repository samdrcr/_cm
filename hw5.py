#范權榮 111210557
class FiniteField:
    def __init__(self, value, p):
        if not self.is_prime(p):
            raise ValueError("Modulus must be prime for a field.")
        self.value = value % p
        self.p = p

    def __add__(self, other):
        return FiniteField(self.value + other.value, self.p)

    def __sub__(self, other):
        return FiniteField(self.value - other.value, self.p)

    def __mul__(self, other):
        return FiniteField(self.value * other.value, self.p)

    def __truediv__(self, other):
        return self * other.inverse()

    def inverse(self):
        # Fermat’s Little Theorem: a^(p-2) mod p is inverse of a mod p
        return FiniteField(pow(self.value, self.p - 2, self.p), self.p)

    def __eq__(self, other):
        return self.value == other.value and self.p == other.p

    def __repr__(self):
        return f"{self.value} (mod {self.p})"

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Example: Field F5
a = FiniteField(2, 5)
b = FiniteField(3, 5)

print("a =", a)
print("b =", b)
print("a + b =", a + b)   # 2 + 3 = 0 mod 5
print("a * b =", a * b)   # 2 * 3 = 1 mod 5
print("a / b =", a / b)   # 2 * inverse(3) = 2*2 = 4 mod 5
