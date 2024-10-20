disk = 1.44
s = 100
st = 50
sym = 25
bfos = 4

space = s * st * sym * bfos
space /= 1024**2

qmod = 1.44 // space
qmod = int(qmod)

# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", qmod)
