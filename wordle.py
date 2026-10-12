import random
import sys

# A handy list of 5-letter secret words
WORDS = [
    "APPLE", "BEACH", "CHAIR", "DREAM", "EAGLE", 
    "FLAME", "GRAPE", "HOUSE", "IMAGE", "JUICE", 
    "KNIFE", "LEMON", "MOUSE", "NIGHT", "OCEAN", 
    "PIANO", "QUEEN", "RADIO", "SMILE", "TRAIN"
]

# ANSI color codes for Wordle-style tiles
GREEN = "\033[42m\033[30m" # Green background, dark text
YELLOW = "\033[43m\033[30m"# Yellow background, dark text
GRAY = "\033[100m\033[30m" # Dark gray background, dark text
RESET = "\033[0m"

def get_color_feedback(guess, secret):
    result = ["gray"] * 5
    secret_chars = list(secret)
    guess_chars = list(guess)

    # First pass: check for exact matches (greens)
    for i in range(5):
        if guess_chars[i] == secret_chars[i]:
            result[i] = "green"
            secret_chars[i] = None
            guess_chars[i] = None

    # Second pass: check for misplaced matches (yellows)
    for i in range(5):
        if guess_chars[i] is not None:
            if guess_chars[i] in secret_chars:
                result[i] = "yellow"
                secret_chars[secret_chars.index(guess_chars[i])] = None
            else:
                result[i] = "gray"
    return result

def print_board_row(guess, feedback):
    row_str = ""
    for char, color in zip(guess, feedback):
        if color == "green":
            row_str += f"{GREEN} {char} {RESET} "
        elif color == "yellow":
            row_str += f"{YELLOW} {char} {RESET} "
        else:
            row_str += f"{GRAY} {char} {RESET} "
    print(row_str)

def main():
    secret = random.choice(WORDS)
    attempts = 6
    
    print("\n==============================")
    print("      TERMINAL WORDLE         ")
    print("==============================\n")
    print("Guess the 5-letter word in 6 tries!\n")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts} - Enter 5-letter word: ").upper().strip()
            if len(guess) == 5 and guess.isalpha():
                break
            print("-> Invalid input. Please enter exactly 5 alphabetic letters.")

        feedback = get_color_feedback(guess, secret)
        print_board_row(guess, feedback)
        print()

        if guess == secret:
            print(f"🎉 Awesome! You guessed the word '{secret}' in {attempt} tries!\n")
            return

    print(f"💀 Game Over! The secret word was: {secret}\n")

if __name__ == "__main__":
    main()
