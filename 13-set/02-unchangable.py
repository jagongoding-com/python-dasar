# anggota set harus dari tipe data yang immutable
set_buah = { 'mangga', 'lemon', 'alpukat', True, 1, 2, 3 }

# kita bisa menjadikan tuple anggota karena ia bersifat immutable
papan_ketik = {
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9),
  (0)
}

# Tapi kita tidak bisa memasukkan list sebagai anggota set
# karena list bersifat mutable
x = { 35, 100, ['a', 'b'] }