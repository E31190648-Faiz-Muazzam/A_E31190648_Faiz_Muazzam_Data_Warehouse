def ikiFunctionSu(ikiVariabelSu):
    ikiConvertDicSu = ikiVariabelSu.keys()
    ikiListSu = list(ikiConvertDicSu)
    return ikiListSu
# ikiFunctionSu()
ikiDataneSu = {
    "1" : "Faiz Muazzam",
    "2" : "Naufal Sulthonul Aziz",
    "3" : "Aji Sampurno",
    "4" : "Budi",
    "5" : "Imam",
    "6" : "Indy Adyib F",
    "7" : "Andy Akbar",
    "8" : "Agus",
    "9" : "Rizky",
    "10" : "David",

}
a = ikiFunctionSu(ikiDataneSu)
print('Hasil Convert List : ')
print(a)
print('Hasil Akhir : ')
print(type(a))