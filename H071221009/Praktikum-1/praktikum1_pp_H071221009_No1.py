## menghitung panjang kapal ##

import math
from re import A

h= float(input('\nMasukkan tinggi menara : '))
a= float(input('Masukkan sudut elevasi pengamat terhadap ujung depan kapal : '))
b= float(input('Masukkan sudut elevasi pengamat terhadap ujung belakang kapal : '))

rad = (math.pi/180)*a
x = math.tan(rad)

rad = (math.pi/180)*b
y = math.tan(rad)

panjang_kapal = round(h*x-h*y,1)
print(panjang_kapal,'m')