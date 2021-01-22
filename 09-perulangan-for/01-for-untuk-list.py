listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

print('Tanpa inumerate:')

for kota in listKota:
  print(kota)

print('\nDengan inumerate:')

for i, kota in enumerate(listKota):
  print(i, kota)