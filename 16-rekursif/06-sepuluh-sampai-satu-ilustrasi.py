i = 1
batas = 3

if i < batas:
  iDua = i + 1
  if iDua < batas:
    iTiga = iDua + 1
    if iTiga < batas:
      iEmpat = iTiga + 1
      if iEmpat < batas:
        iLima = iEmpat + 1
        # dan seterusnya
        print(iLima)
      print(iEmpat)
    print(iTiga)
  print(iDua)
print(i)