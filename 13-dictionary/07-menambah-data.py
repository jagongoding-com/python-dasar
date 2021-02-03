mahasiswa = {
  'nama': 'Lendis Fabri',
  'asal': 'Indonesia',
}

# output None
print('Hobi:', mahasiswa.get('hobi'))
# tambah data
mahasiswa['hobi'] = 'Memancing'
# print ulang
print('Hobi dari {} adalah {}'.format(
  mahasiswa.get('nama'),
  mahasiswa.get('hobi')
))