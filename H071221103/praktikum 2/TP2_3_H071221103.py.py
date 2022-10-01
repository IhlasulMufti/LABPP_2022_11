print ('angka yang paling besar')

a = input('input nilai_a = ')

b = input('input nilai_b = ')

c = input('input nilai_c = ')

if a > b and a > c:
    print (a, 'adalah nilai terbesar') 
elif b > a and b > c:
    print (b, 'adalah nilai terbesar') 
elif c > a and c > b:
    print (c,'adalah nilai terbesar') 
else:
    ('nilai tidak ada')
