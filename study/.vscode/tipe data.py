# tipe data integer (angka)
data_int = 2
print("data: ", data_int, "bertipe data: ", type(data_int))

#tipe data float (pecahan/berkoma)
data_float = 3.5
print("data: ", data_float)
print("- bertipe: ", type(data_float))

#tipe data string (karakter)
data_string = "cie"
print("data: ", data_string)
print("- bertipe: ", type(data_string))

#tipe data boolean
data_bool = True
print("data: ", data_bool)
print("- bertipe: ", type(data_bool))

#tipe data kompleks

data_kompleks = complex(3,6)
print("data: ", data_kompleks)
print("- bertipe: ", type(data_kompleks))

#tipe data dari bahasa C

from ctypes import c_double

data_c_doubke = c_double((13.7))
print("data: ", data_c_doubke)
print("- bertipe: ", type(data_c_doubke))



