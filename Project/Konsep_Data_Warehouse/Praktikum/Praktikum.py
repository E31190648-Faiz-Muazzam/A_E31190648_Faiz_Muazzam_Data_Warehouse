print("=========================Statement===================")
print("Hello Word")
print("Halo dan halo")
print("Halo Teman-teman semester 4")
print("=========================Sting and Case=========================")
judul = "Dengan petik 2"
print(judul)
print("=====================Block of Code=============================")
if 5 > 2:
    print("Selamat Belajar")
    print("Semangat Ya")
print("===================Variabel===============================")
panjang = 100
lebar = 20.5
nama = "Faiz Muazzam"
print(panjang)
print(lebar)
print(nama)
# Variabel untuk mendefinisikan nilai
x = y = z = 3
print(x,y,z)
print("======================Data Type (Integer Float)============================")
x = 5
print("Bilanagan " ,x, "Tipenya adalah ", type(x))
y = 2.5
print("Bilanagan " ,x, "Tipenya adalah ", type(y))
print("======================Data Type (String)============================")
kalimat = "Saya adalah Programmer Python"
print(kalimat[0])
print(kalimat[-1])
print(kalimat[4:12])
print(kalimat[:11])
print("======================Data Type (List)============================")
# List Akan Di ulas pada pertemuan berikutnya
a = [5,10,15,20,25,30,35,40]
print(a[6])
print("======================Data Type (Tuple)============================")
a = (255,255,255)
print(a[0])
print("======================Data Type (Set)============================")
my_set = {1,2,3,4,4}
print(my_set)
print("======================Operator (Penjumlahan)============================")
print("Hasil 13 + 2 = ",13 + 2)
apel = 7
jeruk = 9
buah = apel + jeruk
print("Hasil Apel + Jeruk = Buah = ",buah)
print("======================Operator (Pengurangan)============================")
hutang = 100000
bayar = 75000
sisa = hutang - bayar
print("Sisa Hutang Adalah ",sisa)
print("======================Operator (Perkalian)============================")
panjang = 10
lebar = 7
luas = panjang * lebar
print("Hasil Luas yang di dapat adalah ",luas,"m")
print("======================Operator (Pembagian)============================")
kue = 20
anak = 5
bagi1 = kue / anak
bagi2 = kue // anak
print("Setiap anak mendapat kue sebanyak",bagi2)
print("======================Operator (Modulus)============================")
bil1 = 10
bil2 = 8
hasilModulus = bil1 % bil2
print("Sisa Bagi",bil1,"dengan",bil2,"adalah",hasilModulus)
print("======================Operator (Pangkat)============================")
angka = 5
pangkat = 3
hasilPangkat = angka ** pangkat
print("Hasil",angka,"pangkat",pangkat,"adalah",hasilPangkat)
print("======================Pernyataan If Else============================")
nilai = 9
if (nilai > 7):
    print("Kemampuan Anda Sudah Cukup")
if (nilai > 8):
    print("Kemampuan Anda Sudah Melampaui Batas")

print("======================Pernyataan If Else============================")
nilai = 9
if (nilai < 7):
    print("Kemampuan Anda Kurang")
else:
    print("Kemampuan Anda Sudah Melampaui Batas")
print("======================Pernyataan If Else============================")
hari_ini = "Minggu"
if(hari_ini == "Senin"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Selasa"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Selasa"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Rabu"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Kamis"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Jum'at"):
    print("Saya Kuliah Bos!")
elif(hari_ini == "Sabtu"):
    print("Alhamdulilah Libur")
elif(hari_ini == "Minggu"):
    print("Alhamdulilah Libur")
print("======================For Loop============================")
nomor = [1,2,3,4,5]
print("Hasil Perulangan :")
for i in nomor:
    print(i)
print("======================For Loop (Range)============================")
ulang = 10
print("Hasil Perulangan :")
for i in range(ulang):
    print("Perulangan ke-"+str(i))