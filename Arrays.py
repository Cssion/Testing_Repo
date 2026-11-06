#Mahreza 2607484

import numpy as np

suhu = np.array([30,31,32,32,33,32,30,29,32,31])
nomor = 0

#Melihat suhu selama 10 hari dalam bentuk celcius
for x in suhu:
    nomor += 1
    print(f"Suhu hari ke-{nomor} adalah {x} celcius")


print("\n")
nomor = 0

#Melihat suhu selama 10 hari terakhir dalam bentuk farenheit

for y in suhu:
    nomor += 1
    print(f"Suhu hari ke-{nomor} adalah {(y * 1.8) + 32:.0f} farenhrit")