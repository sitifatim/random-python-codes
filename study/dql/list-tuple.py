bulan_pembelian = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',
                   'Agustus', 'September', 'Oktober', "November", 'Desember']
print(bulan_pembelian[1])
print(bulan_pembelian[2])
print(bulan_pembelian[3])
print(bulan_pembelian[4])

bulan_pembelian = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',
                   'Agustus', 'September', 'Oktober', "November", 'Desember']
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[0:4]
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)
print(bulan_pembelian[-4:-1])

list_makanan = ['Gado-gado','Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

#>>>>>>>>>>>>>>>>>>>>>>>>list manipulation

# Fitur .append()
print(">>> Fitur .append()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.append('Ketoprak')
print(list_makanan)
# Fitur .clear()
print(">>> Fitur .clear()")
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan.clear()
print(list_makanan)
# Fitur .copy()
print(">>> Fitur .copy()")
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
list_makanan2.append('Opor')
list_makanan3.append('Ketoprak')
print(list_makanan1)
print(list_makanan2)
# Fitur .count()
print(">>> Fitur .count()")
list_score = ['Budi', 'Sud', 'Budi', 'Budi', 'Budi', 'Sud', 'Sud']
score_budi = list_score.count('Budi')
score_sud = list_score.count('Sud')
print(score_budi) # akan menampilkan output 4
print(score_sud) # akan menampilkan output 3
# Fitur .extend()
print(">>> Fitur .extend()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu.extend(list_minuman)
print(list_menu)