def tampilkanAngka (batas, i = 1):
  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

  print(f'Perulangan ke {i}')

# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(10)