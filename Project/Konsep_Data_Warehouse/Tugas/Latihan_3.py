# Membuat Kalkuator Sederhana
bilangan1 = input('Masukkan Bilangan 1 : ')
bilangan2 = input('Masukkan Bilangan 2 : ')
print("Pilih opsi ")
print("1. Perkalian")
print("2. Pembagian")
print("3. Penjumlahan")
print("4. Pengurangan")
opsi = input('Pilih Operasi menggunakan angka di atas : ')
option = int(opsi)
if (option == 1):
    hasil = int(bilangan1) * int(bilangan2)
    print(hasil)
elif (option == 2):
    hasil = int(bilangan1) / int(bilangan2)
    print(hasil)
elif (option == 3):
    hasil = int(bilangan1) + int(bilangan2)
    print(hasil)
elif (option == 4):
    hasil = int(bilangan1) - int(bilangan2)
    print(hasil)
