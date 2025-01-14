G = 6.672 * 10**-11

def hitung_gaya_gravitasi(m1, m2, r):
 return G * m1 * m2 *2 / r**2

def hitung_interaktif():
 m1=int(input('Masukkan m1 '))
 m2=int(input('Masukkan m2 '))
 r=int(input('Masukkan r '))
 F=hitung_gaya_gravitasi(m1, m2, r)
 print('Gaya gravitasi: ', F)

print(G)
print(hitung_gaya_gravitasi(100,200,2))
print(hitung_gaya_gravitasi(75, 85, 4))
print(hitung_interaktif())