print('Selamat pagi Andi')
# Selamat pagi Andi

print('Selamat pagi', 'Budi!')
# Selamat pagi Budi!

print('Selamat', 'pagi', 'Doni!')
# Selamat pagi Doni!

print('Andi', 'Budi', 'Tasya', 'Lala')
# Andi Budi Tasya Lala

print('Andi', 'Budi', 'Tasya', 'Lala', sep='_^_')
# Andi_^_Budi_^_Tasya_^_Lala

print('1', '2', '3', sep="*", end="@")
# 1*2*3@

print('1', '2', '3', sep="🐢", end="🦖\n")#
# 1🐢2🐢3🦖

a = 5
b = 3

print(a, '+', b, '=', a + b)
# 5 + 3 = 8

print('{} + {} = {}'.format(a, b, a + b))
# 5 + 3 = 8

print('{} dan {}'.format('Huda', 'Budi'))
# Huda dan Budi

print('{1} dan {0}'.format('Huda', 'Budi'))
# Budi dan Huda

print('Halo {namaDepan} {namaBelakang}'
  .format(namaDepan='Agus', namaBelakang='Priyono'))
# Halo Agus Priyono

# begini juga bisa:
print('Halo {namaDepan} {namaBelakang}'
  .format(
    namaBelakang='Priyono',
    namaDepan='Agus'
  )
)
# Halo Agus Priyono