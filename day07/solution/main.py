from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

chosen_word = random.choice(word_list)
w_len = len(chosen_word)

end_game = False
lives = 6
print("===================================")
print(logo3)
print("\You have 6 chances, rescue the hostage.\n")

display = []
wrong_guesses = []
for _ in range(w_len):
    display += "_"

while not end_game:
    print(f" Lives remaining: {lives}")
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"You've already guessed with the letter '{guess}', pick another letter.")
    else:
        wrong_guesses.append(guess)    

        for posi in range(w_len):
            letter = chosen_word[posi]
            if letter == guess:
                display[posi] = letter

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_game = True
            print("\nGeninus, genius, genius! You won!")
            print(logo2)

        if not end_game:
            print(stages[lives])
            if guess not in chosen_word:
                lives -= 1
                print(f"'{guess}' is not in the word, you lost 1 life. Lives remaining: {lives}")

        if lives == 0:
            end_game = True
            print(stages[lives])
            print("The man has been hung, you lose.")
            print(f"\nThe word was '{chosen_word}'")
