import random

print("=====PERMAINAN BATU GUNTING KERTAS=====\n")
while True:
    player = input('Masukkan pilihan Anda (Batu, Gunting, Kertas) : ')
    if player != "Gunting" and player != "gunting" and player != "Kertas" and player != "kertas" and player != "Batu" and player != "batu":
        print("Masukkan huruf yang sesuai!")

    else:
        com = random.choice(["Kertas", "Batu", "Gunting"])
        print(f"Anda memilih {player} Komputer memilih {com}")

        if (player == "Kertas" or player == "kertas" and com == "Batu") or (player == "Batu" or player == 'batu' and com == "Gunting") or (player == "Gunting" or player == "gunting" and com == "Kertas"):
            print("Anda Menang!")
        elif player == com: print("Seri!")
        elif (player == "kertas" and com == "Kertas") or (player == 'batu' and com == "Batu") or (player == "gunting" and com == "Gunting"): print("Seri!")
        else: print("Anda Kalah")

    play = input("\nIngin main lagi?\nYa / Tidak: ")
    if play == "Tidak" or play == "tidak": print("Terima Kasih sudah bermain!"), exit()
    elif play != "Ya" and play != "ya" and play != "Iya" and play != "iya": print("Pilih sesuai pilihan yang tersedia!"), exit()
