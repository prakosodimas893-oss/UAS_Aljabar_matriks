def tambah_matriks(A, B):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil


def transpose_matriks(A):
    hasil = []
    for i in range(2):
        baris = []
        for j in range(2):
            baris.append(A[j][i])
        hasil.append(baris)
    return hasil


def kali_matriks(A, B):
    hasil = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil