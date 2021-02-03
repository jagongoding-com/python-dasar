mahasiswa = {
  'nama': 'Wahid Abdullah',
  'usia': 18,
  'asal': 'Indonesia'
}

del mahasiswa['nama']
mahasiswa.pop('usia')
mahasiswa.pop('asal')


print("-----------------")

pesan_singkat = {
  "isi": "ISI PESAN INI HANYA BISA DIBACA SEKALI SAJA!! 😱"
}

isi_pesan = pesan_singkat.pop('isi')

# akses langsung dari dictionary
# ouput: None
print('isi pesan:', pesan_singkat.get('isi'))

# akses dari hasil kembalian yang telah disimpan
print('isi pesan:', isi_pesan)