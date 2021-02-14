himpunan = {'maya', 'budi', 100, ('a', 'b'), False, True}
print(himpunan)

# akan error jika nilai 100 tidak ada di dalam set
himpunan.remove(100)
print(himpunan)

# tidak akan error jika ('a', 'b') tidak ada di dalam set
himpunan.discard(('a', 'b'))
print(himpunan)

# remove nilai yang ada di sebelah kiri
nilaiYangDihapus = himpunan.pop()
print('nilaiYangDihapus =', nilaiYangDihapus)
print(himpunan)

# hapus semua nilai
himpunan.clear()
print(himpunan)

