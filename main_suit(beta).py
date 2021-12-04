import random
while True:
    player = input('Masukkan pilihan Anda (Batu, Gunting, Kertas) : ')
    if player != "Gunting" and player != "gunting" and player != "Kertas" and player != "kertas" and player != "Batu" and player != "batu":
        print("Masukkan huruf yang sesuai!")

    else:
        com = random.choice(["Kertas", "Batu", "Gunting"])
        print(f"Anda memilih {player} Komputer memilih {com}")

        if (player == "Kertas" and com == "Batu") or (player == "Batu" and com == "Gunting") or (player == "Gunting" and com == "Kertas"):
            print("Anda Menang!")
        elif player == com: print("Hasilnya Seri")
        else: print("Anda Kalah")
    play = input("Ingin main lagi?\n Ya atau Tidak : ")
    if play == "Tidak" or play == "tidak": print("Terima Kasih sudah bermain"), exit()
