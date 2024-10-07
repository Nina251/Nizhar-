kosong = ""
baris = 9

while baris > 0:
    kolom = baris
    while kolom > 0:
        kosong = kosong + " * "
        kolom = kolom - 1

    kosong = kosong + "\n"
    baris = baris - 1
print(kosong)