print('menghitung panjang kapal')

h = float (input('masukkan ketinggian menara : '))
a = int (input('masukkan sudut elevasi terhadap ujung depan kapal : '))
b = int (input('masukkan sudut elevasi terhadap ujung belakang kapal : '))

import math
rad = (math.pi/180)*a
tan_a=math.tan(rad)

rad = (math.pi/180)*b
tan_b=math.tan(rad)

ac = tan_a*h
bc = tan_b*h

ab = float(ac-bc)
print ('panjang kapal : ', round(ab,1), 'm')