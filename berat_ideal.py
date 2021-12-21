def rumus(berat, tinggi):
    return berat / (tinggi**2)

print("kalkulator bmi".rjust(30).upper())

berat = int(input("Masukkan berat badan Anda(kg) : "))
tinggi = float(input("Masukkan tinggi badan Anda(m) : "))

print('''
 Ketentuan Nilai
<18,5 = Berat badan kurang proporsional
18,5 - 22,9 = Berat badan normal
23 - 29,9 = Berat badan berlebih (Berpotensi Obesitas)
>30 = Obesitas
''')
ideal = rumus(berat, tinggi)
print(f"Nilai untuk Berat Badan Anda {rumus(berat, tinggi):.2f}")
if ideal < 18.5:
    print("Berat Badan Anda kurang proporsional")
elif ideal >= 18.5 and ideal <= 22.9:
    print("Berat Badan Anda normal")
elif ideal >= 23 and ideal <= 29.9:
    print("Berat Badan Anda berlebih (Berpotensi Obesitas)")
elif ideal >= 30:
    print("Anda Obesitas")
