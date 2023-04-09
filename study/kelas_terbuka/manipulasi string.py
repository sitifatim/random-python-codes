nama_depan = "naila"
nama_akhir = "asyani"
nama_lengkap = nama_depan + " " + nama_akhir
print(nama_lengkap)

#indexing
print("index ke -0: " + nama_lengkap[0])
print("index ke -6: " + nama_lengkap[6])
print("index ke[0:3]: ", nama_lengkap[0:3])
print("index ke[0,2,4,6]", nama_lengkap[0:11:2])

#item terkecil
print("paling kecil: "+min(nama_lengkap))
#item terbedar
print("paling besar: "+max(nama_lengkap))

#operator dalam bentuk method
data = "saya suka sama dia"
jumlah = data.count('a') #dalam kode ini yg method adalah count()
print("jumlah a pada " + data + " adalah: " + str(jumlah))


