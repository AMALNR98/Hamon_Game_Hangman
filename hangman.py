from pickle import TRUE
import random
ALREADY_GUESSED_LETTER = 1
WRONG_LETTER           = 2
CORRECT_LETTER         = 3
GAME_LOST              = 5
GAME_WON               = 6
START_GAME             = 7


def get_random_word(dictionary_path="/usr/share/dict/words"):
    '''To get a random word from dictionary'''
    file_for_random_word = open(dictionary_path).readlines()
    while TRUE:
        random_word = random.choice(file_for_random_word).strip()
        if len(random_word) >= 6 and random_word.isalpha() and not random_word[0].isupper():
            return random_word


def masked_word(random_word, guesses):
    hidden_word = ''
    for letter in random_word:
        if letter in guesses:
            hidden_word += letter
        else:
            hidden_word += '-'
    return hidden_word


def turns(new_letter, guesses, turns_left, secret_word):
    if turns_left == 0:
        return turns_left, guesses, GAME_LOST
    if new_letter in guesses:
        return turns_left, guesses, ALREADY_GUESSED_LETTER
    if secret_word == masked_word(secret_word, guesses + [new_letter, ]):
        return turns_left, guesses, GAME_WON

    guesses = guesses + [new_letter, ]

    if new_letter not in secret_word:
        turns_left -= 1
        display = WRONG_LETTER
    else:
        display = CORRECT_LETTER
    return turns_left, guesses, display


def display_board(turns_left, secret_word, guesses, result):
    '''Display currently gussed word, previous guesses
     and current status of the game'''
    print(guesses)
    result_for_display = f"""guess: {" ".join(guesses)}
        {masked_word(secret_word, guesses)}
        turns_left: {turns_left}"""

    if result == START_GAME:
        return "Enter the guess"
    if result == CORRECT_LETTER:
        return "You entered correct letter\n" + result_for_display
    if result == ALREADY_GUESSED_LETTER:
        result_for_display = "You already guessed that letter\n"
        return result_for_display
    if result == WRONG_LETTER:
        result_for_display = "You entered a wrong letter\n"
        return result_for_display

    if result == GAME_WON:
        result_for_display = f"""
        


                                    _______You Won!!!_______
                                    The word is {secret_word}


                        
        
        """
        return result_for_display
    else:
        result_for_display = f"""



                                    ________You Lost!!!_______
                                    The word is {secret_word}
        
        
        
        """
        return result_for_display


def main():
    '''main function for hangman game'''
    turns_left = 7
    secret_word = get_random_word()
    guesses = []
    print(secret_word)
    result = START_GAME
    while True:
        print(display_board(turns_left=turns_left,
              secret_word=secret_word, guesses=guesses, result=result))
        new_letter = input(">>> guess a letter:")
        turns_left, guesses, result = turns(
            new_letter, guesses, turns_left, secret_word)

        if result == GAME_WON:
            print(display_board(turns_left, secret_word, guesses, result))
            break
        if result == GAME_LOST:
            print(display_board(turns_left, secret_word, guesses, result))
            break


if __name__ == "__main__":
    main()
