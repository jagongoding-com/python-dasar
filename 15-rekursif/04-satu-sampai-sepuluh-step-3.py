def tampilkanAngka (batas, i = 1):
  print('Perulangan ke', i)

  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

# memanggil fungsi tampilanAngka
# untuk pertama  kali
tampilkanAngka(10)