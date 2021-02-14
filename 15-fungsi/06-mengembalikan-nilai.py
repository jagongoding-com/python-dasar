def luas_persegi (sisi):
  return sisi * sisi

# tidak menghasilkan output apa pun
luas_persegi(10)

# menghasilkan output
print('Luas persegi dengan sisi 4 adalah:', luas_persegi(4))

# kita juga bisa simpan di dalam variabel
persegi_besar = luas_persegi(100)
persegi_kecil = luas_persegi(50)

print('Toal luas persegi besar dan kecil adalah:', persegi_besar + persegi_kecil)