import re

listKota = [
  'Solo', 'Surabaya', 'Bekasi', 'Jakarta'
]

listHurufVokal = [
  'a', 'i', 'u', 'e', 'o'
]

for kota in listKota:
  print('[' + kota + ']')
  
  for vokal in listHurufVokal:
    print('-->', re.sub('[aiueo]', vokal, kota))
  
