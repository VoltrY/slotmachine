import random
import time
from random import randint

def spinning():
    symbols = ['⚽','⚾','🏈', '🎾', '🕹️']
    spins = ['/', '|', '\\']
    for _ in range(2):
        i = 0
        for symbol in symbols:
            print(f"\r{random.choice(symbols)}"
                  f"  {spins[i]}  "
                  f"   {random.choice(symbols)}"
                  f"   {spins[i]}  "
                  f"   {random.choice(symbols)}")
            time.sleep(0.15)
            i+=1
            if i > 2:
                i = 0


def spin_row():
    symbols = ['⚽','⚾','🏈', '🎾', '🕹️']
    results = []

    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    time.sleep(0.75)
    print("**************")
    print(" | ".join(row)) #join dizideki listedeki her değişkenin yanına o karakteri ekler
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '⚽':
            return bet * 3
        elif row[0] == '⚾':
            return bet * 4
        elif row[0] == '🏈':
            return bet * 5
        elif row[0] == '🎾':
            return bet * 10
        elif row[0] == '🕹️':
            return bet * 20
    if row[0] == row [1] or row[0] == row[2] or row[1] == row[2]:
        return bet * 2
    return 0


def main():
    print("***********************")
    print("Slot oyununa hos geldin")
    print("⚽ | ⚾ |  🏈 | 🎾 | 🕹️")
    balance = 100
    working = True

    while working:
        print("***********************")
        print(f"Mevcut bakiyeniz: ₺{balance}")
        print("***********************")

        bet = input("Oynamak istediğiniz miktarı girin: ")
        if not bet.isdigit():
            print("Lütfen sadece sayı giriniz")
            continue

        bet = int(bet)

        if bet>balance:
            print("Bakiyenizden fazla oynayamazsınız")
            continue
        if bet <= 0:
            print("Negatif oynayamazsınız")
            continue
        balance -= bet

        row = spin_row()
        print("Donuyor...")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"₺{payout} kazandiniz!")
        else:
            print("Kaybettiniz!")

        balance += payout

        play_again = input("Tekrar oynamak ister misin? e/h: ")
        if play_again.lower() != 'e':
            break


    print("***********************")
    print("Tekrar Bekleriz")

if __name__ == '__main__':
    main()
