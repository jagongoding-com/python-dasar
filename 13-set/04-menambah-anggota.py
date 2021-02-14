himpunan_abjad = {'a', 'b', 'c'}
print(himpunan_abjad)

# menambah satu-satu
himpunan_abjad.add('d')
himpunan_abjad.add('e')

# menambah lebih dari satu anggota sekaligus
himpunan_abjad.update({ 'f', 'g' })
# bisa juga pakai list
himpunan_abjad.update(['h', 'i'])

print(himpunan_abjad)