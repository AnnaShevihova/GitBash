
1) Создать переменную типа String

d = "home"
print(type(d), d)

'str'> home

2) Создать переменную типа Integer

a = 2
print(type(a), a)

'int'> 2

3) Создать переменную типа Float

e = 1,5
print(type(e), e)

'tuple'> (1, 5)

4) Создать переменную типа Bytes

i = bytes(22)
print(type(i), i)

'bytes'> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

5) Создать переменную типа List

r = list('Anna')
print(type(r), r)

class 'list'> ['A', 'n', 'n', 'a']

6) Создать переменную типа Tuple

m = tuple('Anna')
print(type(m), m)

'tuple'> ('A', 'n', 'n', 'a')

7) Создать переменную типа Set

k = set('home')
print(type(k), k)

'set'> {'o', 'm', 'h', 'e'}

8. Создать переменную типа Frozen set

l = frozenset('home')
print(type(l), l)

'frozenset'> frozenset({'o', 'm', 'h', 'e'})
