def persentase (total, jumlah):
  if (total >= 0 and total <= jumlah):
    return total / jumlah * 100
  
  return False

# output 50
print(persentase(30, 60))

# output False
print(persentase(100, 60))