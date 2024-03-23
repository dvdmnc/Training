import random

CHOICES = ['rock','paper','scissors']
PLAYER_WIN = {'rock':'scissors','paper':'rock','scissors':'paper'}
DRAW = {'rock':'rock','paper':'paper','scissors':'scissors'}

def game():
    print('winning Rules of the Rock paper and scissor game as follows: \nrock vs paper->paper wins \nrock vs scissors->rock wins \npaper vs scissors->scissors wins ')
    while True:
        computer_choice = CHOICES[random.randint(1,3)]
        print('Enter choice \n1. Rock \n2. paper \n3. scissor ')
        while True:
            choice = input('User choice : ')
            if choice.isnumeric() and len(choice) == 1 and 0<int(choice)<4:
                player_choice = CHOICES[int(choice)-1]
                print(f'User choice is {player_choice}')
                break
            else:
                print('Please enter a valid answer')
                continue
        print(f'Computer chose {computer_choice}')
        print(f'{player_choice} vs {computer_choice}')
        if (f'{player_choice}',f'{computer_choice}') in PLAYER_WIN.items():
            print(f'{player_choice} wins => you win !')
        elif (f'{player_choice}',f'{computer_choice}') in DRAW.items():
            print(f'It\'s a draw !')
        else:
            print(f'{computer_choice} wins => computer wins !')
        
        while True:
            new_game = input('Do you want to play again ? (Y/N)')
            if new_game.isalpha() and len(new_game) == 1:
                if new_game.lower() == 'y':
                    break
                elif new_game.lower() == 'n':
                    return
            else:
                print('Please enter a valid answer (Y/N)')
                continue
        
        
if __name__=='__main__':
    game()

