grup_smp = {
  'andi', 'budi', 'ratna', 'sari'
}

grup_sma = {
  'putri', 'ratna', 'andi', 'agus'
}

# union alias gabungan
print('union:')
print(grup_smp | grup_sma) # cara 1
print(grup_smp.union(grup_sma)) # cara 2

# intersection alias irisan
print('\nintersection')
print(grup_smp & grup_sma) # cara 1
print(grup_smp.intersection(grup_sma)) # cara 2

# difference
print('\nanggota grup smp yang bukan anggota grup sma')
print(grup_smp - grup_sma)
print(grup_smp.difference(grup_sma))

print('\ndibalik, anggota grup sma yang bukan anggota grup smp:')
print(grup_sma - grup_smp)
print(grup_sma.difference(grup_smp))

# symetric_difference
print('\nanggota yang hanya ikut satu grup saja:')
print(grup_sma.symmetric_difference(grup_smp))