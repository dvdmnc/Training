import random

def select_range():
    print("Please select the range to guess from :")
    while True:
        try:
            From = int(input("From: "))
            if From < 0:
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    while True:
        try:
            To = int(input("To: "))
            if From > To:
                print("Please enter a valid number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    
    return [From, To]

def game():
    From, To = select_range()
    choice = random.randint(From, To)
    while True:
        try:
            guess = int(input('Guess the number chosen by the computer: '))
            if From > guess or guess > To:
                print("Please enter a valid number")
                continue
            break
        except:
            print("Please enter a valid number")
    turn_count = 0
    while guess != choice:
        turn_count += 1
        if guess > choice:
            print("You guessed to high, try again")
        else:
            print("You guessed to low, try again")
        while True:
            try:
                guess = int(input('Guess the number chosen by the computer: '))
                if From > guess or guess > To:
                    print("Please enter a valid number")
                    continue
                break
            except:
                print("Please enter a valid number")
    print(f"Good job ! You found the right number : {choice} in {turn_count} turns")

if __name__ == '__main__':
    game()

