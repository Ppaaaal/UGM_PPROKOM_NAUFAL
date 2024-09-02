N = int (input("Masukkan Jumlah Detik: "))
A = 60 * 60 * 24
HARI = N // A
B = A * HARI
C = N - B
JAM = C // (60 * 60)
D = JAM * 60 * 60
E = C - D
MENIT = E // 60
DETIK = N % 60
print ("%d Hari %d Jam %d Menit %d Detik" %(HARI,JAM,MENIT,DETIK))
