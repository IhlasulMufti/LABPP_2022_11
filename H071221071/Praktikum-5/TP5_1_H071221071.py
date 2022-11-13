matriks_1 = []
for i in range(2): #untuk baris
    baris = []
    for j in range(2): #untuk kolom
        baru = int(input(f"Matriks 1 Baris {i + 1} dan Kolom {j + 1} : "))
        baris.append(baru)
    matriks_1.append(baris)
# print(matriks_1)

matriks_2 = []
for i in range(2):
    baris = []
    for j in range(2):
        baru = int(input(f"Matriks 2 Baris {i + 1} dan Kolom {j + 1} : "))
        baris.append(baru)
    matriks_2.append(baris)
# print(matriks_2)

a3 = (matriks_1[0][0]*matriks_2[0][0]) + (matriks_1[0][1]*matriks_2[1][0])
c3 = (matriks_1[1][0]*matriks_2[0][0]) + (matriks_1[1][1]*matriks_2[1][0])
b3 = (matriks_1[0][0]*matriks_2[0][1]) + (matriks_1[0][1]*matriks_2[1][1])
d3 = (matriks_1[1][0]*matriks_2[0][1]) + (matriks_1[1][1]*matriks_2[1][1])
# print ()
print(f'| {matriks_1[0][0]}, {matriks_1[0][1]} | x | {matriks_2[0][0]}, {matriks_2[0][1]} | = | {a3}, {b3} |')
print(f'| {matriks_1[1][0]}, {matriks_1[1][1]} |   | {matriks_2[1][0]}, {matriks_2[1][1]} |   | {c3}, {d3} |')
#[[1 2]   [[5 6]
# [3 4]]   [7 8]]
