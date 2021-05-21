def tampilkanAngka (batas, i = 1):
  prefix = '--' * (i - 1)

  print(f'{prefix} Sebelum rekursif ({i})')
  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

  print(f'{prefix} Setelah rekursif ({i})')

# memanggil fungsi tampilkanAngka
# untuk pertama  kali
tampilkanAngka(5)