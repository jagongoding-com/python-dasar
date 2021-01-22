## 0 sampai 4
for i in range(5):
  print("Perulangan ke -", i)

print('------------')

## 10 sampai 15
for i in range(10, 16):
  print('i =', i)

print('------------')

## Bilangan genap kelipatan 2
for i in range(2, 12, 2):
  print('i =', i)

print('------------')

## Bilangan ganjil kelipatan 2
for bilangan_ganjil in range(1, 12, 2):
  print(bilangan_ganjil)

print('------------')

## Range dengan enumerate
for urutan, nilai in enumerate(range(100, 200, 15)):
  print('Perulangan ke', urutan, '=', nilai)