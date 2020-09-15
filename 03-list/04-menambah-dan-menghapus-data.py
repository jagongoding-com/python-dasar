list_buah = ['Jeruk', 'Naga', 'Pepaya', 'Mangga']
print(list_buah)

# tambah data di belakang list
list_buah.append('Sirsak')
print(list_buah)

# tambah data di awal list
list_buah.insert(0, 'Jambu')
print(list_buah)

# tambah data di index mana pun dalam list
list_buah.insert(2, 'Manggis')
print(list_buah)

print('\n' * 2)

list_angka = [1, 2, 3, 4, 5]
print(list_angka)

# hapus satu angka di belakang
angka_yang_terhapus = list_angka.pop()

print('angka yang terhapus:', angka_yang_terhapus)
print(list_angka)

print('\n' * 2)

list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)

# hapus item pertama dengan nilai 'Jambu'
list_buah.remove('Jambu')
print(list_buah)

print('\n' * 2)

list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu']
print(list_buah)

del list_buah[1]
print(list_buah)

del list_buah[0:2]
print(list_buah)
