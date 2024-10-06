n = int(input("Masukkan jumlah data: "))

total = 0

for i in range(n):
    data = float(input(f"Masukkan data ke-{i+1}: "))
    total += data

rata_rata = total / n

print(f"Rata-rata dari {n} data yang dimasukkan adalah: {rata_rata}")
