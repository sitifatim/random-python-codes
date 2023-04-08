#memasukan data dari user

data = input("masukkan data: ")
print("data: ", data, ",type data: ", type(data))

#apabila tidak di casting di awal, tipe data dari inputan auto string
data_int = int(input("masukan data integer: "))
print("data: ", data_int," bertipe: ", type(data_int))

#mengambil data bool 
bolean = bool(int(input("masukan data:")))
print("data: ", bolean," bertipe: ", type(bolean))