#范權榮 111210557
"""
Geometry Module
----------------
This script implements fundamental geometric operations and objects using Python 3.

It includes:
- Classes: Point, Line, Circle, Triangle
- Functions for intersection calculations (lines, circles, line-circle)
- Function for finding the foot of a perpendicular
- Function for verifying the Pythagorean theorem
- Transformation methods for geometric objects

Mathematical Principles:
------------------------
1. Line Equation: ax + by + c = 0
2. Circle Equation: (x - h)^2 + (y - k)^2 = r^2
3. Distance Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
4. Rotation Formula:
   x' = x*cosθ - y*sinθ
   y' = x*sinθ + y*cosθ
5. Pythagorean Theorem: a² + b² = c² for right triangles
"""

import math


# ===============================
# BASIC GEOMETRIC OBJECTS
# ===============================

class Point:
    """Represents a point in 2D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        """Translate point by (dx, dy)."""
        return Point(self.x + dx, self.y + dy)

    def scale(self, factor):
        """Scale point by a factor relative to the origin."""
        return Point(self.x * factor, self.y * factor)

    def rotate(self, angle_deg):
        """Rotate point around the origin by angle in degrees."""
        angle_rad = math.radians(angle_deg)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Point(x_new, y_new)

    def distance_to(self, other):
        """Return Euclidean distance between this point and another."""
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x:.2f}, {self.y:.2f})"


class Line:
    """Represents a line in the form ax + by + c = 0."""
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_points(cls, p1, p2):
        """Create a Line passing through two points."""
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = -(a * p1.x + b * p1.y)
        return cls(a, b, c)

    def __repr__(self):
        return f"Line({self.a}x + {self.b}y + {self.c} = 0)"


class Circle:
    """Represents a circle with center (h, k) and radius r."""
    def __init__(self, h, k, r):
        self.h, self.k, self.r = h, k, r

    def __repr__(self):
        return f"Circle(center=({self.h}, {self.k}), r={self.r})"


# ===============================
# GEOMETRIC OPERATIONS
# 范權榮 111210557
# ===============================

def intersect_lines(L1, L2, epsilon=1e-9):
    """Return intersection point of two lines or None if parallel or identical."""
    det = L1.a * L2.b - L2.a * L1.b
    if abs(det) < epsilon:
        return None  # Parallel or coincident
    x = (L2.b * (-L1.c) - L1.b * (-L2.c)) / det
    y = (L1.a * (-L2.c) - L2.a * (-L1.c)) / det
    return Point(x, y)


def intersect_circles(C1, C2, epsilon=1e-9):
    """Return intersection points (list of Point) of two circles."""
    d = math.hypot(C2.h - C1.h, C2.k - C1.k)
    if d > C1.r + C2.r or d < abs(C1.r - C2.r) or abs(d) < epsilon:
        return None  # No intersection or infinite (coincident) circles

    # Distance from center1 to the line joining intersection points
    a = (C1.r**2 - C2.r**2 + d**2) / (2 * d)
    h = math.sqrt(max(C1.r**2 - a**2, 0))
    # Midpoint on the line between centers
    x2 = C1.h + a * (C2.h - C1.h) / d
    y2 = C1.k + a * (C2.k - C1.k) / d

    # Intersection points
    rx = -(C2.k - C1.k) * (h / d)
    ry = (C2.h - C1.h) * (h / d)

    p1 = Point(x2 + rx, y2 + ry)
    p2 = Point(x2 - rx, y2 - ry)

    if p1.distance_to(p2) < epsilon:
        return [p1]  # Tangent circles
    return [p1, p2]


def intersect_line_circle(L, C, epsilon=1e-9):
    """Return intersection point(s) between a Line and a Circle."""
    a, b, c = L.a, L.b, L.c
    h, k, r = C.h, C.k, C.r

    # Substitute line equation into circle equation
    if abs(b) < epsilon:  # Vertical line x = constant
        x = -c / a
        delta = r**2 - (x - h)**2
        if delta < 0:
            return None
        elif abs(delta) < epsilon:
            return [Point(x, k)]
        else:
            y1 = k + math.sqrt(delta)
            y2 = k - math.sqrt(delta)
            return [Point(x, y1), Point(x, y2)]
    else:
        # Express y in terms of x and substitute into circle equation
        A = 1 + (a**2 / b**2)
        B = 2 * (a * c / b**2 + a * h / b - k)
        Cq = h**2 + (c**2 / b**2) + (2 * c * k / b) + k**2 - r**2
        discriminant = B**2 - 4 * A * Cq
        if discriminant < 0:
            return None
        elif abs(discriminant) < epsilon:
            x = -B / (2 * A)
            y = (-a * x - c) / b
            return [Point(x, y)]
        else:
            sqrt_d = math.sqrt(discriminant)
            x1 = (-B + sqrt_d) / (2 * A)
            x2 = (-B - sqrt_d) / (2 * A)
            y1 = (-a * x1 - c) / b
            y2 = (-a * x2 - c) / b
            return [Point(x1, y1), Point(x2, y2)]


def perpendicular_foot(L, P):
    """Return the foot of perpendicular from point P to line L."""
    a, b, c = L.a, L.b, L.c
    denom = a**2 + b**2
    x = (b * (b * P.x - a * P.y) - a * c) / denom
    y = (a * (-b * P.x + a * P.y) - b * c) / denom
    return Point(x, y)


def verify_pythagoras(P, foot, Q, epsilon=1e-6):
    """Verify if P, foot, and Q form a right triangle (Pythagorean theorem)."""
    a = P.distance_to(foot)
    b = Q.distance_to(foot)
    c = P.distance_to(Q)
    return math.isclose(a**2 + b**2, c**2, rel_tol=epsilon)


# ===============================
# TRIANGLE CLASS
# ===============================

class Triangle:
    """Represents a triangle with vertices A, B, C."""
    def __init__(self, A, B, C):
        self.A, self.B, self.C = A, B, C

    def translate(self, dx, dy):
        """Translate the triangle by (dx, dy)."""
        return Triangle(self.A.translate(dx, dy),
                        self.B.translate(dx, dy),
                        self.C.translate(dx, dy))

    def scale(self, factor):
        """Scale the triangle relative to the origin."""
        return Triangle(self.A.scale(factor),
                        self.B.scale(factor),
                        self.C.scale(factor))

    def rotate(self, angle):
        """Rotate the triangle by angle (degrees) around the origin."""
        return Triangle(self.A.rotate(angle),
                        self.B.rotate(angle),
                        self.C.rotate(angle))

    def __repr__(self):
        return f"Triangle({self.A}, {self.B}, {self.C})"


# ===============================
# EXAMPLE USAGE
# 范權榮 111210557
# ===============================
if __name__ == "__main__":
    # Define points, lines, and circles
    P1, P2 = Point(0, 0), Point(4, 4)
    L1 = Line.from_points(P1, P2)
    L2 = Line.from_points(Point(0, 4), Point(4, 0))
    print("Intersection of lines:", intersect_lines(L1, L2))

    C1, C2 = Circle(0, 0, 5), Circle(4, 0, 3)
    print("Intersection of circles:", intersect_circles(C1, C2))

    print("Intersection of line and circle:", intersect_line_circle(L1, C1))

    # Perpendicular foot and Pythagorean theorem
    P = Point(3, 4)
    foot = perpendicular_foot(L1, P)
    print("Foot of perpendicular:", foot)
    print("Pythagorean theorem valid:", verify_pythagoras(P, foot, P1))

    # Triangle transformations
    tri = Triangle(Point(0, 0), Point(4, 0), Point(0, 3))
    print("Original triangle:", tri)
    print("Translated:", tri.translate(2, 1))
    print("Scaled:", tri.scale(2))
    print("Rotated 45°:", tri.rotate(45))
