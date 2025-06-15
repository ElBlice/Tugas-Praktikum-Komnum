import matplotlib.pyplot as plt
import numpy as np
import math

def get_function():
    func_str = input("Masukkan fungsi f(x) (misal: x**3 - x - 2): ")

    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names["x"] = x
        return eval(func_str, {"__builtins__": {}}, allowed_names)

    return f

def regula_falsi(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Metode gagal: f(a) dan f(b) harus memiliki tanda berbeda.")
        return None, []

    iterasi = []
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iterasi.append((i, a, b, c, f(c)))

        if abs(f(c)) < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, iterasi

f = get_function()
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
tol = float(input("Masukkan toleransi (misal: 1e-6): "))
max_iter = int(input("Masukkan jumlah iterasi maksimum: "))

akar, data_iterasi = regula_falsi(f, a, b, tol, max_iter)

print("\nIterasi\t a\t\t b\t\t c\t\t f(c)")
for i, a_i, b_i, c_i, fc_i in data_iterasi:
    print(f"{i}\t {a_i:.6f}\t {b_i:.6f}\t {c_i:.6f}\t {fc_i:.6e}")

if akar is not None:
    print(f"\nAkar yang ditemukan: {akar:.6f}")

    x_vals = np.linspace(a - 1, b + 1, 400)
    y_vals = [f(x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)

    for _, _, _, c_i, _ in data_iterasi:
        plt.plot(c_i, f(c_i), 'ro')
        plt.vlines(c_i, 0, f(c_i), linestyles='dashed', color='red', alpha=0.5)

    plt.title("Visualisasi Metode Regula Falsi")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
