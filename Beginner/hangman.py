import random 
placeholder =  "_"
word_list = ["camel", "hangman", "python", "computer"]
chosen_word = random.choice(word_list)
x = []
print(chosen_word)
print(placeholder*len(chosen_word))
chances = 6
game_over = False
while not game_over:
    guess = input("Enter your guess letter: ").lower()
    print(guess)
    display = ""
    if guess not in chosen_word:
        chances -= 1 
    else: 
        for i in chosen_word:
            if i == guess:
                display += i
                x.append(i)
            elif i in x: 
                display += i
            else:
                display += "_"
    if chances>0:
        print(display)
        print("Number of chances left: ", chances)
    else:
        print("Oops you lost")
        break
    
    

    