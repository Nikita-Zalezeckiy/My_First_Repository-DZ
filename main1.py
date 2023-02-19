from roman import *

y = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
print(y)
for i in y:
    print(i, '->' ,roman_to_int(i))

b=[4, 58, 1994, 26, 99, 69, 80]
for i in b:
    print(i, '->',int_to_roman(i))
