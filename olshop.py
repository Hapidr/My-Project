import pandas as pd
print("yahaha hayuuk fried chicken".upper())

dps = pd.DataFrame(
    {"Jenis":["Dada", "Paha", "Sayap"], "Harga":[5000, 4500, 4500]},
    index=[1,2,3])
print(dps)
print('Anda bisa dapat Diskon 10% jika membeli lebih dari 5 potong')
banyak_jenis = int(input("Beli berapa banyak?  "))
banyak_pesanan = []
for i in range(banyak_jenis):
    print(f"Pesanan ke-{i + 1}")
    jenis_potong = input("Jenis: ")
    if jenis_potong.lower() == 'paha' and jenis_potong.lower() == 'dada' and jenis_potong.lower() == 'sayap':
        banyak_pesanan.append(jenis_potong)
    else:
        print('jenis potongan yang anda masukkan tidak sesuai!')
        exit()

harga = {'dada':1, 'paha':2, 'sayap':3}
total_harga = []
for j in range(banyak_jenis):
    total_harga.append(dps.loc[harga[banyak_pesanan[j]], 'Harga'])

total_harga = sum(total_harga)
if banyak_jenis >= 5:
    total_harga *= 0.1
    print(f'Total belanja anda adalah Rp. {total_harga}')
    exit()

print(f'Total belanja anda adalah Rp. {total_harga}')
