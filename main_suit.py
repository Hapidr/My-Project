import random as rnd

print("PERMAINAN BATU GUNTING KERTAS".center(50, " "))
while True:
    player = input('Masukkan pilihan Anda (Batu, Gunting, Kertas) : ')
    if player.lower() != "gunting" and player.lower() != "kertas" and player.lower() != "batu":
        print("Masukkan huruf yang sesuai!")
    else:
        com = rnd.choice(["Kertas", "Batu", "Gunting"])
        print(f"Anda memilih {player.upper()} Komputer memilih {com.upper()}")
        if (player.lower() == "kertas" and com == "Batu") or (player.lower() == "batu" and com == "Gunting") or (player.lower() == "gunting" and com == "Kertas"):
            print("Anda Menang!")
        elif player.lower() == com.lower(): print("Seri!")
        else: print("Anda Kalah")

    a = 1
    while a == 1:
        play = input("\nIngin main lagi?\nYa atau Tidak: ")
        if play.lower() == "tidak": print("Terima kasih sudah bermain!"), exit()
        elif play.lower() == "ya": 
            a = 2
        else:
            print("Masukkan pilihan yang sesuai!")
