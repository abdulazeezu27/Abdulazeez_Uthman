#  Randomisation and python List
#   2. randint(a,b)
import random

i = 100
j = 200
#  Generates a random number between i and j
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')

c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')
print('i =', i, 'and j =', )
print('randrange() generated number: ', a)
print('randint() generator number ', c)
