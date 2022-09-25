import math  # import math agar bisa memakai pi akar sincostan dll
print('H = ketnggian menara')
print('A = sudut elevasi terhadap ujung belakang kapal')
print('B = sudut elevasi terhadap ujung depan kapal')

h = float(input('Masukkan nilai H : '))
a = float(input('Masukkan nilai A : '))
b = float(input('Masukkan nilai B : '))

x = math.tan(math.radians(a))*h    # a di radiantkan lalu di tan kan
                                  
y = math.tan(math.radians(b))*h    # b di radiantkan lalu di tan kan

panjang_kapal = round(math.sqrt(x-y)**2,1)    # math sqrt untuk akar

print(panjang_kapal,'m')