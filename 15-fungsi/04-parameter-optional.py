def suhu_udara (daerah, derajat, satuan = 'celcius'):
  print("Suhu di {} adalah {} {}".format(daerah, derajat, satuan))

suhu_udara("Surabaya", 30)
suhu_udara("Surabaya", 86, 'Fahrenheit')