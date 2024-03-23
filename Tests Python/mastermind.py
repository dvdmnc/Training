import random
import copy

COLORS = ["Y","G","B","R","P","O","W"]

def game():
    colors = []
    for _ in range(4):
        color = random.choice(COLORS)
        colors.append(color)
    
    print(f'The computer has chosen a combination of 4 colors in the following list {COLORS}')
    print('You have to guess the combination. Write your guesses in this manner, Example : Y G B R')
    print('Good Luck !')

    while True:
        while True:
            guess = input('Your Guess :')
            guess = guess.strip()
            guess = guess.upper()
            if guess.isalpha() and len(list(guess)) == 4:
                guess = list(guess)
                break
            else:
                print('Please enter a valid guess')
        same_col = 0
        same_col_pos = 0
        colors_copy = copy.deepcopy(colors) #We're going to use this copy to avoid comparing digits multiple times by removing them once we found a match at the same index or different index
        for idx, col in enumerate(guess):
            print(colors_copy)
            if col == colors[idx]:
                same_col_pos += 1
                colors_copy[idx] = ' '
                guess[idx] = ' ' #If we don't do that the digit at the right position in guess is also counted in the second loop
        #Once we checked for same position and removed the colors, we can check if there are other colors but not in same position
        for col in guess:
            if col != ' ' and col in colors_copy:  
                index = colors_copy.index(col) 
                colors_copy[index] = ' '
                same_col += 1

        if same_col_pos == 4:
            print('You found the right combination, good job !')
            break
        print(f'You have {same_col} right color(s) and {same_col_pos} color(s) on the right position')


if __name__=='__main__':
    game()