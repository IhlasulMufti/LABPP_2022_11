print('\nMenghitung panjang kapal')

h= float(input('\nMasukkan tinggi menara : '))
a= int(input('Sudut elevasi pengamat terhadap ujung belakang kapal : '))
b= int(input('Sudut elevasi pengamat terhadap ujung depan kapal : '))


import math
rad_a= 3.1415926535898/180*a
tan_a= (math.tan(rad_a))

rad_b= 3.1415926535898/180*b
tan_b= (math.tan(rad_b))

ac= tan_a*h
bc= tan_b*h

ab = (ac-bc)**2
AB = ab**(0.5)

print ('\nPanjang kapal : ', round(AB,1), 'm')
