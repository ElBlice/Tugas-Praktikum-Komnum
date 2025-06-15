import numpy as np
import math

def get_function():
    func_str = input("Masukkan fungsi f(x) (misal: sin(x), x**2 + 1, exp(-x**2)): ")

    def f(x):
        allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed["x"] = x
        return eval(func_str, {"__builtins__": {}}, allowed)

    return f

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum_ = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum_ += f(a + i * h)
    return h * sum_

def romberg_integration(f, a, b, max_iter):
    R = np.zeros((max_iter, max_iter))
    for i in range(max_iter):
        n = 2**i
        R[i, 0] = trapezoidal_rule(f, a, b, n)
        for k in range(1, i + 1):
            R[i, k] = (4**k * R[i, k-1] - R[i-1, k-1]) / (4**k - 1)
    return R

f = get_function()
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
max_iter = int(input("Masukkan jumlah iterasi maksimum (misal: 5): "))

romberg_table = romberg_integration(f, a, b, max_iter)

print("\nTabel Romberg:")
for row in romberg_table:
    print("\t".join(f"{val:.10f}" for val in row))

print(f"\nPerkiraan hasil integrasi: {romberg_table[max_iter-1, max_iter-1]:.10f}")
