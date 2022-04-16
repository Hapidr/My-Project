

def jumlah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def bagi(a, b):
    return a / b

def kali(a, b):
    return a * b

while True:
    print("\nKalkulator sederhana \nPilih Operasi:".title())
    masuk = input("1. Jumlah\n2. Kurang\n3. Bagi\n4. Kali\nTekan 'X' untuk keluar\n")
    if masuk == '1':
        print("\"Tambah +\"")
        a = int(input(" "))
        b = int(input("+\n "))
        print(f'= {jumlah(a, b)}')

    elif masuk == '2':
        print('"Kurang -"')
        a = int(input(' '))
        b = int(input('-\n '))
        print(f'= {kurang(a, b)}')

    elif masuk == '3':
        print('"Bagi ÷"')
        a = int(input(' '))
        b = int(input('÷\n '))
        print(f'= {bagi(a, b)}')

    elif masuk == '4':
        print('"Kali ×"')
        a = int(input(' '))
        b = int(input('×\n '))
        print(f'= {kali(a, b)}')

    elif masuk == 'x'.lower():
        exit()

    else:
        print('Masukkan angka yang benar!')

    

