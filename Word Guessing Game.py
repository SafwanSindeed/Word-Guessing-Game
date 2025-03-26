import random

difficulty_level = input('What difficulty would you like to try: '
                        '\neasy'
                        '\nmedium'
                        '\nhard'
                        '\n-->')

def choose_word(difficulty):
    if difficulty == "easy":
        word_list = ["cat", "dog", "run", "eat"]
    elif difficulty == "medium":
        word_list = ["apple", "table", "chair", "window"]
    elif difficulty == "hard":
        word_list = ["python", "hangman", "puzzle", "library"]
    else:
        print("Invalid difficulty. Using medium difficulty.")
        word_list = ["apple", "table", "chair", "window"]
    return random.choice(word_list)

def give_hint(word, guesses):
    new_guesses = guesses.copy()
    unguessed_positions = [i for i in range(len(word)) if new_guesses[i] == '_']
    
    if not unguessed_positions:
        return None, new_guesses
        
    hint_position = random.choice(unguessed_positions)
    hint_letter = word[hint_position]
    
    for i in range(len(word)):
        if word[i] == hint_letter:
            new_guesses[i] = hint_letter
    return hint_letter, new_guesses

word = choose_word(difficulty_level.lower())
guesses = ['_'] * len(word)
attempts = 4
used_letters = set() 
hint_used = False 

print("\nWelcome to Hangman! You have 4 attempts to guess the word.")
print("Type 'hint' to get a random letter revealed (can only be used once).")

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guesses))
    guess = input('Guess a Letter (or type "hint"): ').lower()
    
    if guess == "hint":
        if not hint_used:
            hint_letter, guesses = give_hint(word, guesses)
            if hint_letter:
                print(f"HINT: Revealed the letter '{hint_letter}'")
                used_letters.add(hint_letter.lower())
                hint_used = True
                
                if '_' not in guesses:
                    print('\nCongratulations!! You guessed the word: ' + word)
                    break
            else:
                print("No more letters to hint!")
        else:
            print("You've already used your hint!")
        continue
    
    if not guess:
        print("Please enter a letter.")
        continue
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in used_letters:
        print("You already guessed that letter. Try another one.")
        continue
    
    used_letters.add(guess)
    
    if guess in word.lower():
        found = False
        for i in range(len(word)):
            if word[i].lower() == guess:
                guesses[i] = word[i]
                found = True
        if found:
            print("Good Guess!")
    else:
        attempts -= 1
        print(f'Wrong Guess. Attempts left: {attempts}')
    
    if '_' not in guesses:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if '_' in guesses:
    print('\nYou\'ve run out of attempts! The word was: ' + word)