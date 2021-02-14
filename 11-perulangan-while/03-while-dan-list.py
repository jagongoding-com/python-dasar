listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

# bermain index
i = 0
while i < len(listKota):
  print(listKota[i])
  i += 1

print('----------------')

# bermain pop
while listKota:
  print(listKota.pop(0))