# Kalkulator sederhana
print(30*"=")
print("\tKalkulator Sederhana")
print(30*"=")

#variabel yang diperlukan dan operatornya
angka1 = float(input("Masukkan angka 1: "))
operator = input("Masukkan operator (+,-,*,/): ")
angka2 = float(input("Masukkan angka2: "))

#percabangan

if operator == "+":
    hasil = angka1 + angka2
    print(f"hasilnya adalah: {hasil:.2f}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"hasilnya adalah: {hasil:.2f}")
elif operator == "x" or operator == '*':
    hasil = angka1 * angka2
    print(f"hasilnya adalah: {hasil:.2f}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasilnya adalah: {hasil:.2f}")
else:
    print("Operator salah")

print(30*"=")
print("\tTerima Kasih")
print(30*'=')

    