import random

words = [
    "apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "zebra", "ocean", "mountain", "river", "valley", "forest", "desert", "island", "canyon",
    "planet", "galaxy", "universe", "nebula", "asteroid", "comet", "meteor", "eclipse", "horizon", "twilight",
    "sunset", "sunrise", "shadow", "glimmer", "sparkle", "thunder", "lightning", "hurricane", "blizzard", "tornado",
    "breeze", "whisper", "echo", "melody", "harmony", "rhythm", "canvas", "palette", "sculpture", "mural",
    "castle", "palace", "mansion", "cottage", "cabin", "fortress", "temple", "pyramid", "monument", "tower",
    "journey", "voyage", "odyssey", "safari", "expedition", "quest", "adventure", "flight", "cruise", "trek",
    "diamond", "emerald", "ruby", "sapphire", "topaz", "amethyst", "quartz", "crystal", "marble", "granite",
    "quantum", "matrix", "vector", "vertex", "fractal", "entropy", "gravity", "velocity", "friction", "inertia"
]
word=random.choice(words)
wordlen=len(word)
guessedword=["-"]*wordlen
guessedletter=[]
lives = 9
stages=[
"""
  +---+
      |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]
print("Hangman")
print("*"*20)
print(f"Guess this{wordlen} letter word if you can! You are left with {lives} chances")
while lives>0:
    print("".join(guessedword))
    guess = input("\n Enter your guess: ").lower()
    if guess in guessedletter:
        print("You already guessed this letter!")
        continue
    guessedletter.append(guess)

    if guess in word:
        for i in range(wordlen):
            if word[i] == guess:
                guessedword[i] = guess
    else:
        lives=lives-1
        print(f"\n Your guess is wrong. You have {lives} chances")
        print(stages[9-lives if(9-lives)<len(stages)else -1])
    if "-" not in guessedword:
        print("\n You Won!!! the word is",word)
        break
if lives == 0:
    print("You lost. the word was ",word)