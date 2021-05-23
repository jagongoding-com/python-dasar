list_a = [1, 2, 3, 4]
set_a = {1, 2, 3, 4}

print('[Sebelum]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')

list_a.remove(2)
list_a.remove(4)

set_a.remove(2)
set_a.remove(4)

print('[Sesudah]')
print(f'  list\t: {list_a}')
print(f'  set\t: {set_a}')
