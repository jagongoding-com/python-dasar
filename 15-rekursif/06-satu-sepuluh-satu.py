def tampilkanAngka (batas, i = 1):
  prefix = '--' * (i - 1)

  print(prefix + 'Sebelum rekursif ({})'.format(i))
  if (i < batas):
    # di sini lah rekursifitas itu terjadi
    tampilkanAngka(batas, i + 1)

  print(prefix + 'Setelah rekursif ({})'.format(i))

# memanggil fungsi tampilanAngka
# untuk pertama  kali
tampilkanAngka(5)