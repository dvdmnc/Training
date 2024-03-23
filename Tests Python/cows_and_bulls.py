import random
import copy

def game():
    to_guess = []
    for _ in range(4):
        to_guess.append(str(random.randint(1,9)))
    
    print(f'The computer has chosen a combination of 4 digits')
    print('You have to guess the combination. Write your guesses in this manner, Example : 1578')
    print('A cow indicates that you have found one digit, a bull that a digit is at the right place. Good Luck !')
    
    while True:
        while True:
            guess = input('Your Guess :')
            if guess.isnumeric() and len(guess) == 4:
                guess = list(guess)
                break
            else:
                print('Please enter a valid value')
                continue
        same_digit = 0
        same_digit_pos = 0
        to_guess_copy = copy.deepcopy(to_guess) #We're going to use this copy to avoid comparing digits multiple times by removing them once we found a match at the same index or different index
        for idx, dig in enumerate(guess):
            if dig == to_guess_copy[idx]:
                same_digit_pos += 1
                to_guess_copy[idx] = ' '
                guess[idx] = ' ' #If we don't do that the digit at the right position in guess is also counted in the second loop
        #Once we checked for same position and removed the digits, we can check if there are other digits but not in same position
        for dig in guess:
            if dig != ' ' and dig in to_guess_copy:
                same_digit += 1
                index = to_guess_copy.index(dig)
                to_guess_copy[index] = ' '
    
        if same_digit_pos == 4:
            print('You found the right combination, good job !')
            break
        print(f'{same_digit} Cow(s) and {same_digit_pos} Bull(s)')


if __name__=='__main__':
    game()