def matriks1(merk, matk):
    for baris in range(2):
        matk_baris = []
        for kolom in range(2):
            nilai_baru = int(input(f'Input nilai matriks {merk} index {baris+1},{kolom+1} :'))
            matk_baris.append(nilai_baru)
        matk.append(matk_baris)
    return matk

result = [[0,0],
          [0,0]]

def hasilkali(matk1, matk2):
    for i in range(2):
        for j in range(2):
            for k in range(2): 
                result[i][j] += (matk1[i][k] * matk2[k][j])
            
    print(' |',  (matk1[0][0]),(matk1[0][1]), '|', 'x', '|', (matk2[0][0]),(matk2[0][1]), '|', '=', '|', (result[0][0]),(result[0][1]), '|')
    print(' |',  (matk1[1][0]),(matk1[1][1]), '|', ' ', '|', (matk2[1][0]),(matk2[1][1]), '|', ' ', '|', (result[1][0]),(result[1][1]), '|')

matk1 = []              
matk2 = []
matk1 = matriks1("pertama", matk1)
matk2 = matriks1("kedua", matk2)
hasilkali(matk1, matk2)