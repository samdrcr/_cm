h_step = 0.00001

def derivative(func, val):
    return (func(val + h_step) - func(val)) / h_step

def integrate(func, start, end):
    x_val = start
    total_area = 0
    while x_val < end:
        total_area += func(x_val) * h_step
        x_val += h_step
    return total_area

def check_theorem(func, point):
    result = derivative(lambda z: integrate(func, 0, z), point)
    print('result =', result, 'func(point) =', func(point))
    print('abs(result - func(point)) < 0.01 =', abs(result - func(point)) < 0.01)
    assert abs(result - func(point)) < 0.01

def my_function(x):
    return x**3

print('derivative(my_function, 2) =', derivative(my_function, 2))
print('integrate(my_function, 0, 2) =', integrate(my_function, 0, 2))

check_theorem(my_function, 2)
