import random


def spin():
    Symbols = ['👌','☠️','🕸️','🤖','👾','👻']

    return [random.choice(Symbols) for _ in range(3)]


def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")


def payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "👌":
            return bet * 5

        elif row[0] == "☠️":
            return bet * 10
        
        elif row[0] == "🕸️":
            return bet * 15
        
        elif row[0] == "🤖":
            return bet * 20
        
        elif row[0] == "👾":
            return bet * 25
        
        elif row[0] == "👻":
            return bet * 30
        
    else:
        return 0


def main():

    balance = 100

    print("****************************")
    print("Welcome to Slot Machine Game")

    print("Symbols: 👌☠️🕸️🤖👾👻")

    print("****************************")

    while balance > 0:

        print(f"Your Current balance is: ${balance}")

        bet = input("Enter the bet amount: ")


        if not bet.isdigit():
            print("Enter a valid input")
            continue

        bet = int(bet)


        if bet > balance:
            print("Insufficient funds")
            play_again = input("Do you want to Spin again (Y/N): ").upper()
            if play_again != "Y":
                break
            else:
                continue

            
        if bet <= 0:
            print("Bet amount should be greater than zero")
            play_again = input("Do you want to Spin again (Y/N): ").upper()
            if play_again != "Y":
                break
            else:
                continue


        balance -= bet
        row = spin()
        print("Spinning.....\n")

        print_row(row)

        amount_won = payout(row,bet)

        if amount_won > 0:
            print(f"Congratulations! You won ${amount_won}")

        else:
            print("Sorry you lost")

        balance += amount_won

        play_again = input("Do you want to Spin again (Y/N): ").upper()


        if play_again != "Y":
            break
        
if __name__ == '__main__':
    main()