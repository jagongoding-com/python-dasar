kota = 'Lamongan'

def halo () :
  print(kota)

print('[print secara langsung]', kota)
print('[panggil fungsi halo]', end=' ')

halo()

print('**************')

kota, provinsi = 'Lamongan', 'Jawa Timur'

def hello ():
  provinsi = 'Jawa Barat'
  print(kota, provinsi)

print('[PANGGIL FUNGSI hello()]')
hello()

print('\n[SECARA LANGSUNG]')
print(kota, provinsi)