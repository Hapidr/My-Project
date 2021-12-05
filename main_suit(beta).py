import random

print("=====PERMAINAN BATU GUNTING KERTAS=====\n")
while True:
    player = input('Masukkan pilihan Anda (Batu, Gunting, Kertas) : ')
    if player.lower() != "gunting" and player.lower() != "kertas" and player.lower() != "batu":
        print("Masukkan huruf yang sesuai!")

    else:
        com = random.choice(["Kertas", "Batu", "Gunting"])
        print(f"Anda memilih {player.upper()} Komputer memilih {com.upper()}")

        if (player.lower() == "kertas" and com == "Batu") or (player.lower() == "batu" and com == "Gunting") or (player.lower() == "gunting" and com == "Kertas"):
            print("Anda Menang!")
        elif player.lower() == com.lower(): print("Seri!")
        else: print("Anda Kalah")

    play = input("\nIngin main lagi?\nYa / Tidak: ")
    if play.lower() == "tidak": print("Terima kasih sudah bermain!"), exit()
    elif play.lower() != "ya": print("Masukkan pilihan yang sesuai!"), exit()
