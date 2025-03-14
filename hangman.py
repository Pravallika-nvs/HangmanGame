import random

# Word list
words = ["apple", "ball", "cat", "dog", "fish", "grape", "hat", "ice", "juice", "kite",
         "lamp", "moon", "nest", "orange", "pencil", "queen", "rose", "sun", "tree", "umbrella",
         "breeze", "candle", "dragon", "elephant", "feather", "guitar", "horizon", "island",
         "jungle", "knight", "lantern", "meadow", "notebook", "octopus", "pyramid", "quiver",
         "rainbow", "squirrel", "tornado", "voyage", "astronaut", "benevolent", "catastrophe",
         "diligence", "effervescent", "formidable", "gargantuan", "haphazard", "idiosyncratic",
         "juxtaposition", "kaleidoscope", "labyrinth", "metamorphosis", "nefarious", "obfuscate",
         "paradoxical", "quintessential", "rendezvous", "serendipity", "transcendent"]

# Choose a random word
secret_word = random.choice(words)

# Initialize the game state
word_display = ["_"] * len(secret_word)  # Placeholder for the word
attempts = 6  # Number of allowed wrong guesses
guessed_letters = []  # Store guessed letters

# Display initial underscores
print("\nWord to guess:", " ".join(word_display))

while attempts > 0 and "_" in word_display:
    # Get user input
    while True:
        guess = input("\nEnter a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.append(guess)
            break  # Valid input
        print("Invalid input! Enter a single unused letter.")

    # Check if guess is in the word
    if guess in secret_word:
        print("Good job! The letter is in the word.")
        for index, letter in enumerate(secret_word):
            if letter == guess:
                word_display[index] = letter
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

    # Display updated word
    print(" ".join(word_display))

    # Check for win condition
    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

# If user runs out of attempts
if attempts == 0:
    print("\n😢 You ran out of attempts! The word was:", secret_word)
