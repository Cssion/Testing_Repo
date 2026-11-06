# 2. Algoritma Bubble Sort (urut dari terbesar ke terkecil)
def bubblesort(arr):
    data = arr.copy()          
    n = len(data)
    for i in range(n - 1):
        ada_tukar = False
        for j in range(n - 1 - i):
            if data[j] < data[j + 1]:          # jika kiri lebih kecil
                data[j], data[j + 1] = data[j + 1], data[j]
                ada_tukar = True
        if not ada_tukar:                      
            break
    return data
