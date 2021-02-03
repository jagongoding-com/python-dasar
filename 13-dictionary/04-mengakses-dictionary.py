pertemuan_hari_ini = {
  "judul": "Belajar Dictionary Pada Python 3",
  "tanggal": "01 Februari 2021",
  "kategori": [
    "Python", "Python Dasar"
  ],
  "page_views": 10,
  "published": True,
  "share_count": {
    "facebook": 0,
    "twitter": 2
  }
}

print('Judul:', pertemuan_hari_ini.get('judul'))
# atau
print('Tanggal:', pertemuan_hari_ini['tanggal'])

# bisa menggunakan fungsi berantai untuk dictionary bertingkat
print('Facebook share:', pertemuan_hari_ini.get('share_count').get('facebook'))
# bisa juga dengan kurung siku dua-duanya
print('Twitter share:', pertemuan_hari_ini['share_count']['twitter'])

share_count = pertemuan_hari_ini.get('share_count')
# ini error
# print('Instagram share:', share_count['instagram'])

# sedangkan ini tidak error
print('Instagram share:', share_count.get('instagram', 0))