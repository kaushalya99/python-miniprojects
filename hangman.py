import random

words=['python', 'java', 'ruby', 'go', 'javascript', 'swift']

#Randomly choose a word from the list
choosen_word = random.choice(words)
word_display = ['_' for _ in choosen_word]  #create a list of underscores
attempts = 8 #Number of allowed attempts

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in choosen_word:
