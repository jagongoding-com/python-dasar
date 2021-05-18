max_baris = 7
max_kolom = 7

baris = 0
while baris < max_baris:
  kolom = 0
  while kolom < max_kolom:
    print('o' if kolom <= baris else '+', end = ' ')
    kolom += 1
  else:
    print('')
  baris += 1

