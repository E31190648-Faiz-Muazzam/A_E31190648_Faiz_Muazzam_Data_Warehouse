# memanggil class Modul_Operasi
import Modul_Operasi
# menjalankan fungsi yang ada di class Modul_Operasi
Modul_Operasi.tambah(1,2)
Modul_Operasi.kurang(1,2)

# memanggil class Modul_Operasi dan menyimpannya dengan nama matematika
import Modul_Operasi as matematika
# menjalankan fungsi yang ada di class Modul_Operasi
matematika.tambah(1,3)
matematika.kurang(1,3)

# hanya menjalankan 1 fungsi
from Modul_Operasi import tambah
tambah(1,2)

# dapat menjalankan 2 fungsi
from Modul_Operasi import tambah,kurang
tambah(1,2)
kurang(1,2)

# dapat menjalankan semua fungsi
from Modul_Operasi import *
tambah(1,2)
kurang(1,2)
