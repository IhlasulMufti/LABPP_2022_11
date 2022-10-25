index0 = int(input('Input nilai matriks pertama index 1,1 : '))
index1 = int(input('Input nilai matriks pertama index 1,2 : '))
index2 = int(input('masukkan nilai matriks pertama index 2,1 : '))
index3 = int(input('masukkan nilai matriks pertama index 2,2 : '))
index4 = int(input('masukkan nilai matriks kedua index 1,1 : '))
index5 = int(input('masukkan nilai matriks kedua index 1,2 : '))
index6 = int(input('masukkan nilai matriks kedua index 2,1 : '))
index7 = int(input('masukkan nilai matriks kedua index 2,2 : '))

matriks1 = [
    [index0,index1],
    [index2,index3]]

matriks2 = [
    [index4,index5],
    [index6,index7]]

hasil = []
for i in range(len(matriks1)):
    sementara = []
    for j in range(len(matriks1)):
       total = 0
       for k in range(len(matriks1)):
        total = total + (matriks1[i][k] * matriks2[k][j])
       sementara.append(total)
    hasil.append(sementara)     
for i in hasil:
    print(i)