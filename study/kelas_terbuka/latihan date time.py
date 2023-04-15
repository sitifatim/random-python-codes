import datetime as dt

print("Silakan masukan tahun \nbulan dan tanggal")

tahun = int(input("masukan tahun: "))
bulan = int(input("masukan bulan: "))
tanggal = int(input("masukan tanggal: "))

hari_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir adalah: {hari_lahir}")
print(f"hari lahir adalah hari: {hari_lahir:%A}")

#menghitung umur
hari_ini = dt.date.today()
umur = hari_ini - hari_lahir
banyak_umur = umur.days // 365
print(f"umur anda adalah {banyak_umur} tahun")
