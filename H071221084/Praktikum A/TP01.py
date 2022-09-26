import math 
from re import A

h = int(input('Masukkan nilai H : '))
a = int(input('Masukkan nilai A : '))
b = int(input('Masukkan nilai B : '))

rad = (math.pi/180)*a
x = math.tan(rad)

rad = (math.pi/180)*b
y = math.tan(rad)

panjang_kapal = round(h*x-h*y,1)

print(panjang_kapal,'m')