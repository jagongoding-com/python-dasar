def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
  print("Suhu di {} adalah {} {}".format(daerah, derajat, satuan))

suhu_udara('Jakarta', 'fahrenheit')
suhu_udara('Jakarta', satuan = 'fahrenheit')
suhu_udara(satuan='kelvin', daerah='Makasar', derajat=100)