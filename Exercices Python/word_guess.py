import random

WORDS = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

def game():
    name= input('What\'s your name ? ')
    print(f'Good luck {name}!')
    choice = random.choice(WORDS) 
    guessed_list = ['_']*len(choice) 
    print('Guess the characters')
    for letter in guessed_list:
        print(letter)
    guessed = 0
    while guessed < len(guessed_list):
        while True: #Loop to check if the input is a valid one
            guess = input('Guess a character : ')
            if guess.isalpha() and len(guess) == 1: #Is a char and only one char
                break
            else:
                print('Enter a valid Character')
                continue
        if guess in choice:
            start = 0
            end = len(choice)
            while True: #Check for multiple occurences of a char in the word
                try:
                    index = choice.index(guess, start, end)
                    if guessed_list[index] != guess:
                        guessed_list[index] = guess
                        guessed += 1
                        break
                    start = index + 1
                except ValueError: #.index raise ValueError if the char is not found (if all occurences already found, then the index will search in a substring that doesn't contain the char we're looking for at one point because of the start increasing)
                    print('All occurences of this character already found')
                    break
        else:
            print('This character is not in the word')
        for letter in guessed_list:
            print(letter)
    print('You win !')
    print(f'The word was {choice}')

if __name__=='__main__':
    game()