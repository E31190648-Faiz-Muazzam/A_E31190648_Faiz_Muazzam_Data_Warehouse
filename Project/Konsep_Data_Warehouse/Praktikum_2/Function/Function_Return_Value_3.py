# Rumus : Sisi x Sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus : sisi x sisi x sisi
def volume_kubus(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume
print("Hasil Luas Persegi : ")
print(luas_persegi(5))
print("Hasil Luas Volume Kubus : ")
print(volume_kubus(5))