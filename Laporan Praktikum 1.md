# Praktikum 1 Komnum
|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241184 | Naufaldi Faqih Abimanyu  |
| 5025241211 | Rafi Putra Rosadi |
| 5025241212 | Akmal Yusuf |

## Soal
Anda sudah mengerti algoritma pemrosesan metode Regula Falsi, dan anda sudah memahami cara kerjanya. Sekarang anda tinggal mengimplementasikan algoritma tersebut menjadi sebuah program komputer metode Regula Falsi (yang dapat menampilkan proses iteratif numerik, lengkap dengan grafik fungsinya). 

## Deskripsi

Program ini merupakan implementasi dari metode *Regula Falsi* (False Position Method) dalam Python untuk mencari akar dari suatu fungsi kontinu. Selain mencari akar, program juga memvisualisasikan proses iterasi dalam bentuk grafik menggunakan library `matplotlib`.

---

## Persyaratan

Sebelum menjalankan program, pastikan telah menginstal:

```bash
pip install matplotlib numpy
```

---

## Struktur Program

### 1. Import Library

```python
import matplotlib.pyplot as plt
import numpy as np
import math
```

### 2. Input Fungsi oleh Pengguna

Fungsi dibaca dalam bentuk string lalu dievaluasi menggunakan `eval` secara aman.

```python
def get_function():
    func_str = input("Masukkan fungsi f(x) (misal: x**3 - x - 2): ")
    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names["x"] = x
        return eval(func_str, {"__builtins__": {}}, allowed_names)
    return f
```

### 3. Fungsi `regula_falsi`

Melakukan iterasi metode regula falsi hingga memenuhi toleransi atau jumlah iterasi maksimum.

```python
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
```

### 4. Visualisasi

Menampilkan grafik dari fungsi serta titik-titik iterasi akar.

```python
plt.plot(x_vals, y_vals, label='f(x)', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.plot(c_i, f(c_i), 'ro')
plt.vlines(c_i, 0, f(c_i), linestyles='dashed', color='red', alpha=0.5)
```

---

## Contoh Input

```bash
Masukkan fungsi f(x) (misal: x**3 - x - 2): x**3 - x - 2
Masukkan nilai a: 1
Masukkan nilai b: 2
Masukkan toleransi (misal: 1e-6): 1e-6
Masukkan jumlah iterasi maksimum: 50
```

---

## Contoh Output

```text
Iterasi	 a		 b		 c		 f(c)
0	 1.000000	 2.000000	 1.333333	 -0.962963e+00
1	 1.333333	 2.000000	 1.462687	 -4.218262e-01
2	 1.462687	 2.000000	 1.504019	 -1.461348e-01
...
Akar yang ditemukan: 1.521380
```

Grafik juga akan muncul secara visual menampilkan kurva fungsi dan titik-titik pendekatan akar pada setiap iterasi.

---

## Penutup

Program ini bermanfaat untuk memahami bagaimana metode regula falsi bekerja dan bagaimana pendekatan numerik dilakukan untuk mencari akar fungsi non-linear.

---
