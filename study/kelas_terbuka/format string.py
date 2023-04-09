#format string

#string
nama = "angel"
format_str = f"hello {nama}" #tanda format diawali dengan f"
print(format_str)

#int
#dengan menggunakan format string maka angka tidak perlu
#diubah dengan casting string jika ingin ditampilkan
angka = 30.4
format_str = f"angka = {angka}"
print(format_str)

#bilangan bulat
angka = 15
format_str = f"bilangan bulat: {angka:d}"
print(format_str)

#jutaan
angka = 50000000
format_str = f"jutaan: {angka:,}"
print(format_str)

#pecahan
angka = 34.567578
format_str = f"pecahan: {angka:.3f}"
print(format_str)

#menampilkan landing zero
angka = 23.4556
format_str = f"landing zero: {angka:06.2f}"
print(format_str)

# menampilkan tanda -/+
neg = -9
pos = 9.98593
format_neg = f"negatif: {neg}"
format_pos = f"positif: {pos:+.3f}"
print(format_neg)
print(format_pos)

#persen
persen = 0.344556
format_str = f"persen: {persen:.2%}"
print(format_str)

#format angka lain binary/octal/hexadecimal
angka = 255
format_bin = f"binary: {bin(angka)}"
format_oc = f"octal: {oct(angka)}"
format_hex = f"hexadecimal: {hex(angka)}"

print(format_bin)
print(format_oc)
print(format_hex)

#operasi aritmatika pada format string
harga = 100000
jumlah = 3
format_str = f"harga total : {harga*jumlah:,}"
print(format_str)
