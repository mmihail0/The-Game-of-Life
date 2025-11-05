previous_guesses = []
solution = []
streak = 0


word = input("Enter the word to be guessed: ")
lives = int(input("Enter the number of lives you want: "))
for i in range(len(word)):
    if word[i] == " ":
        solution.append(" ")
    else:
        solution.append("_")
guess = ""

def game(guess, word, lives, previous_guesses, solution, streak):
    while guess != word:
        guess = input("Enter your guess: ")
        if guess in previous_guesses:
            print(f"Youve already tried {guess} before, try something else")
            previous_guesses.append(guess)
            continue
        if guess == word:
            print("You guessed the word correctly! well done")
            streak += 1
            print(f"Your streak is at {streak} right now")
            break
        elif guess in word and len(guess) == 1:
            print(f"Good guess, the letter {guess} is in the word")
            for i in range(len(word)):
                if word[i] == guess:
                    solution[i] = guess
        else:
            lives -= 1
            print(f"{guess} is incorrect")
            if lives == 1:
                print("You have 1 more incorrect attempt before you lose")
            elif lives == 0:
                print(f"You have lost, the word was {word}")
                print(f"Your streak was {streak}")
                streak = 0
                break
            else:
                print(f"You now have {lives} lives remaining")
        previous_guesses.append(guess)

        if "_" not in solution:
            print("You guessed the word correctly! well done")
            streak += 1
            print(f"Your streak is at {streak} right now")
            break

        print("Your current information looks like: ")
        print(*solution)
    return streak, lives

streak, lives = game(guess, word, lives, previous_guesses, solution, streak)
play_again = input("Do you want to play again? yes or no: ").lower()
while play_again == "yes":
    if play_again == "no":
        break
    previous_guesses = []
    solution = []
    word = input("Enter the word to be guessed: ")
    for i in range(len(word)):
        if word[i] == " ":
            solution.append(" ")
        else:
            solution.append("_")
    guess = ""
    if streak != 0:
        cont_lives = input("Do you want to continue with the number of lives you had last round?").lower()
        if cont_lives == "yes":
            streak, lives = game(guess, word, lives, previous_guesses, solution, streak)
        else:
            lives = int(input("Enter the number of lives you want: "))
            streak, lives = game(guess, word, lives, previous_guesses, solution, streak)
    else:
        lives = int(input("Enter the number of lives you want: "))
        streak, lives = game(guess, word, lives, previous_guesses, solution, streak)
    play_again = input("Do you want to play again? yes or no: ").lower()
