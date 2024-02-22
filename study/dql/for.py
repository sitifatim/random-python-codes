list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)


list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

# For loops with break
print("For loops with break")
total_tagihan_break = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan_break += tagihan
print("Total tagihan %d." % total_tagihan_break)
print()

# For loops with continue
print("For loops with continue")
total_tagihan_continue = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" % tagihan)
        continue
    total_tagihan_continue += tagihan
print("Total tagihan %d." % total_tagihan_continue)


list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)

list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran) 
print(total_pemasukan)

# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
# Pengecekan kendaraan dengan nomor pelat ganjil atau genap 
# Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
kendaraan_genap = 0
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += 1
    else:
        kendaraan_ganjil += 1
# Total pengeluaran untuk kendaraan dengan nomor pelat ganjil 
# dan genap dalam 1 bulan
i = 1
total_pengeluaran = 0
while i <= jumlah_hari:
    if i % 2 == 0:
        total_pengeluaran += (kendaraan_genap * uang_jalan)
    else:
        total_pengeluaran += (kendaraan_ganjil * uang_jalan)
    i += 1
# Cetak total pengeluaran
print(total_pengeluaran)