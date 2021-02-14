buah_yang_tersedia = ['jeruk', 'mangga', 'melon']
buah_yang_dicari = input('Masukkan nama buah dalam huruf kecil: ')

if (buah_yang_dicari in buah_yang_tersedia):
  print('Buah yang anda cari tersedia!')
else:
  print('Buah yang anda cari tidak tersedia!')