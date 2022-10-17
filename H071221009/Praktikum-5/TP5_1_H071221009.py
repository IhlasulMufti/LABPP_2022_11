# Program mengalikan 2 buah matriks 2x2

def matriks1(label, mat):
    for baris in range(2):
        mat_baris = []
        for kolom in range(2):
            elemen_baru = int(input(f'Input nilai matriks {label} index {baris+1},{kolom+1} :'))
            mat_baris.append(elemen_baru)
        mat.append(mat_baris)
    return mat

result = [[0,0],
          [0,0]]

def hasilkali(mat1, mat2):
    for i in range(2):
        for j in range(2):
            for k in range(2): 
                result[i][j] += (mat1[i][k] * mat2[k][j])
            
    print(' |',  (mat1[0][0]),(mat1[0][1]), '|', 'x', '|', (mat2[0][0]),(mat2[0][1]), '|', '=', '|', (result[0][0]),(result[0][1]), '|')
    print(' |',  (mat1[1][0]),(mat1[1][1]), '|', ' ', '|', (mat2[1][0]),(mat2[1][1]), '|', ' ', '|', (result[1][0]),(result[1][1]), '|')

mat1 = []
mat2 = []
mat1 = matriks1("pertama", mat1)
mat2 = matriks1("kedua", mat2)
hasilkali(mat1, mat2)