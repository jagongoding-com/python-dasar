def suhu_udara (daerah, derajat = 30, satuan = 'celcius'):
  print(f"Suhu di {daerah} adalah {derajat} {satuan}")

suhu_udara('Jakarta', 'fahrenheit')
suhu_udara('Jakarta', satuan = 'fahrenheit')
suhu_udara(satuan='kelvin', daerah='Makasar', derajat=100)