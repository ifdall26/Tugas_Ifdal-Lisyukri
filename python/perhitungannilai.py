# #perhitungan rata-rata nilai

# Nilai_A = float(input('Masukkan Nilai A : '))
# Nilai_B = float(input('Masukkan Nilai B : '))
# Nilai_Akhir = (Nilai_A + Nilai_B) /2
# print(Nilai_Akhir)

kehadiran = float(input('Masukkan Nilai Kehadiran : '))
UTS = float(input('Masukkan Nilai UTS : '))
UAS = float(input('Masukkan Nilai UAS : '))
Nilai_Akhir = ((30/100) * UTS) + ((50/100) * UAS) + ((20/100) * kehadiran) 
print(Nilai_Akhir)