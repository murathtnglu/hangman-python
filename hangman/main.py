import random
from words import words_list
from words import stages

chosen_word = random.choice(words_list)
display = []
end_of_game = False
lives = 6

for letters in chosen_word:
    display.append("_")
print(display)

while not end_of_game:
    if("_" in display):
        guess = input("Guess a letter").lower()
        for i in range(len(chosen_word)):
            if(chosen_word[i] == guess):
                display[i] = guess
                print(display[i],end=" ")

            else:
                print(display[i],end=" ")


        if guess not in chosen_word:
            lives-=1
            if(lives == 0):
                print(f"\nYOU LOSE! The chosen word was {chosen_word}")
                end_of_game = True

        print(stages[lives])
    else:
        print("\nYOU WON!")
        end_of_game = True