listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

print('Tanpa enumerate:')

for kota in listKota:
  print(kota)

print('\nDengan enumerate:')

for i, kota in enumerate(listKota):
  print(i, kota)