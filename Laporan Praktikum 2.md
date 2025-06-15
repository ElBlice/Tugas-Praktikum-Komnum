# Praktikum 2 Komnum
|    NRP     |      Name      |
| :--------: | :------------: |
| 5025241184 | Naufaldi Faqih Abimanyu  |
| 5025241211 | Rafi Putra Rosadi |
| 5025241212 | Akmal Yusuf |

## Soal 

Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut.

## Deskripsi Program

Program ini mengimplementasikan metode Romberg Integration, yaitu penyempurnaan dari metode Trapezoida dengan menggunakan ekstrapolasi Richardson untuk meningkatkan akurasi hasil integral.
Program menerima input fungsi dari pengguna secara interaktif menggunakan eval(), lalu menghitung nilai integral dengan pendekatan bertingkat (dalam bentuk tabel Romberg).

## Penjelasan metode

- Metode Trapezoida digunakan untuk menghitung nilai awal integral dengan berbagai pembagian 
𝑛 = 2^𝑖

- Romberg Table dibentuk dengan menyimpan hasil tersebut dan mengaplikasikan ekstrapolasi Richardson :
![imagealt](https://github.com/xaldinzz/read.me/blob/main/Screenshot%202025-06-15%20205228.png?raw=true)
- Semakin tinggi iterasi, semakin akurat hasil integrasi terhadap nilai eksak.


## Cuplikan Kode phyton
import numpy as np
import math
```
def get_function():
    func_str = input("Masukkan fungsi f(x): ")
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
```

## pembahasan code

### get_function() – Input Fungsi dari Pengguna :
Tujuan:
- Meminta pengguna memasukkan fungsi, misalnya x**2, sin(x), exp(-x**2)
- Fungsi eval() digunakan untuk mengevaluasi string sebagai ekspresi Python (dengan keamanan terbatas)
- Fungsi f(x) yang dikembalikan bisa langsung dipakai di perhitungan nanti.

### trapezoidal_rule(f, a, b, n) – Hitung Integral Trapezoida
Tujuan:

-Menghitung nilai integral dengan metode trapezoida biasa

-Parameter:
-- f: fungsi yang diintegrasi
-- a, b: batas bawah dan atas
-- n: jumlah subinterval (jumlah potongan trapezoida)

### romberg_integration(f, a, b, max_iter) – Buat Tabel Romberg
Tujuan:
- Menggunakan hasil trapezoida dengan berbagai n untuk membentuk tabel Romberg
- Setiap baris i merepresentasikan pembagian n = 2^i
- Elemen R[i][k] dihitung dari elemen sebelumnya menggunakan ekstrapolasi Richardson

## Contoh input dan output
 - Step 1:
```
 Masukkan fungsi f(x) (misal: sin(x), x**2 + 1, exp(-x**2)):
```
   untuk output ini aku akan memasukan exp(x)
 - Step 2:
```
Masukkan batas bawah (a):
```
untuk output ini aku akan memasukan: 0

- Step 3:
```
Masukkan batas atas (b):
```
untuk output ini aku akan memasukan: 1

- Step 4:
```
Masukkan jumlah iterasi maksimum (misal: 5):
```
untuk output ini aku akan memasukan: 5

- Step 5:
untuk step ke lima ini dia akan mengeluarkan output seperti ini:
```
Tabel Romberg:
1.8591409142					
1.7188611519	1.7183188419			
1.7183182280	1.7182819741	1.7182818287	
1.7182819741	1.7182818286	1.7182818285	1.7182818285	
1.7182818286	1.7182818285	1.7182818285	1.7182818285	1.7182818285
```
- Output akhir: Perkiraan hasil integrasi: 1.7182818285

## Kesimpulan

Dalam praktikum ini, kami telah berhasil mengimplementasikan metode Romberg Integration menggunakan bahasa Python. Metode ini merupakan penyempurnaan dari metode trapezoida yang menggabungkan hasil integral numerik secara bertingkat menggunakan ekstrapolasi Richardson.

Melalui input interaktif berupa fungsi matematika, batas bawah dan atas integrasi, serta jumlah iterasi maksimum, program mampu menghitung nilai aproksimasi integral dengan tingkat akurasi tinggi meskipun menggunakan jumlah titik yang relatif kecil.

Berdasarkan hasil uji coba seperti integrasi dari fungsi e^x pada interval [0,1], diperoleh hasil mendekati nilai eksak 
𝑒 − 1≈1.718281828, menunjukkan bahwa program berjalan dengan akurat dan stabil.
