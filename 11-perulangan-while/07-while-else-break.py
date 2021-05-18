listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Masukkan nama kota yang dicari: ')

i = 0
while i < len(listKota):
  if listKota[i].lower() == kotaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan', listKota[i])
  i += 1
else:
  print('Maaf, kota yang anda cari tidak ditemukan.')
  