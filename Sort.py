#Mahreza 2607484

import numpy as np

nilai = np.array([
    78, 85, 92, 67, 74, 88, 95, 60, 81, 70,
    89, 73, 97, 65, 84, 77, 91, 58, 86, 79,
    93, 69, 82, 75, 90, 63, 87, 72, 98, 80
])




nilai_terurut = bubblesort(nilai)


print("\nNilai setelah diurutkan (terbesar -> terkecil):")
print(nilai_terurut)

lima_terbesar = nilai_terurut[:5]
print("\n5 Nilai terbesar:")
print(lima_terbesar)

for i, n in enumerate(lima_terbesar, start=1):
    print(f"Peringkat {i}: {n}")