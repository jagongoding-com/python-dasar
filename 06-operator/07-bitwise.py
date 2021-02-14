a = 1
b = 64

print('a =', a, '=', format(a, '08b'))
print('b =', b, '=', format(b, '08b'), '\n')

print('[and]')
print('a & b =', a & b)
print(format(a, '08b'), '&', format(b, '08b'), '=', format(a & b, '08b'), '\n')

print('[or]')
print('a | b =', a | b)
print(format(a, '08b'), '|', format(b, '08b'), '=', format(a | b, '08b'), '\n')

print('[xor]')
print('a ^ b =', a ^ b)
print(format(a, '08b'), '^', format(b, '08b'), '=', format(a ^ b, '08b'), '\n')

print('[not]')
print('~a ~b =', ~a, ~b)
print('~' + format(a, '08b'), '~' + format(b, '08b'), '=', format(~a, '08b'), format(~b, '08b'), '\n')

print('[shift right]')
print('a >> b =', a >> b)
print(format(a, '08b'), '>>', format(b, '08b'), '=', format(a >> b, '08b'), '\n')

print('[shift left]')
print('b << a =', b << a)
print(format(b, '08b'), '<<', format(a, '08b'), '=', format(b << a, '08b'), '\n')