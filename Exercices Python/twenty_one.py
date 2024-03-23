def player_turn(values):
    print('Your Turn')
    while True:
        quantity = input('How many numbers do you wish to enter ? \n')
        if quantity.isdigit() and 0 < int(quantity) < 4: #Is a number between 1 and 3
            print('Enter your values :')
            for _ in range(int(quantity)):
                while True: #Check for valid input
                    value = input('')
                    if value.isdigit() and 0 < len(value) < 3: #Is a number, only one number (one or two digits)
                        if int(value) == 21 and len(values) == 20: #Player lost
                            print('Computer won')
                            return True
                        elif len(values) == 0 and int(value) == 1: #First element of the game needs to be a 1
                            values.append(int(value))
                            break
                        elif values[-1]+1 == int(value): #The new value follow the last one ?
                            values.append(int(value))
                            break
                        else:
                            print('Please enter valid values :')
                            continue
                    else:
                        print('Please enter valid values : ')
                        continue
            break
        else:
            print('Please enter valid value')
            continue
    
    return False

def computer_turn(values):
    quantity = 3
    if len(values) == 0:
        values.append(1)
        quantity -= 1
    elif values[-1] == 20:
            print('You won, congratulations !')
            return True
    count = 0
    for _ in range(quantity):
        if count > 0 and values[-1]%4 == 0:
            break
        else:
            count += 1
            values.append(values[-1]+1)
    print('Order of inputs after computer\'s turn is:')
    print(values)
    return False



def game():
    print('Enter F to take the first chance')
    print('Enter S to take the second chance')
    values = []
    while True:
        start = input('')
        if start == 'F':
            lost = player_turn(values)
            turn = 'c'
            break
        elif start == 'S':
            lost = computer_turn(values)
            turn = 'p'
            break
        else:
            print('Please enter a valid answer')
    
    while not lost:
        if turn == 'c':
            lost = computer_turn(values)
            turn = 'p'
        else:
            lost = player_turn(values)
            turn = 'c'


if __name__=='__main__':
    print('Player 2 is computer')
    while True:
        play = input('Do you want to start the game ? (Yes/No) ')
        if play.lower() == 'yes':
            game()
            break
        elif play.lower() == 'no':
            continue
        else:
            print('Please enter a valid answer')
            