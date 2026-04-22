attempts = 0

import random
number = random.randint(1, 100)

while True:
    guess = input("Guess a number (Type 'exit' to quit): ")
    if guess == 'exit':
        break

    guess = int(guess)
    attempts +=1

    if guess == number:
        print(f"Congratss!! You got it with {attempts} attempts!! 🎉")
        play_again = input("Play again? (yes/no): ")
        if play_again == 'yes':
            attempts = 0
            number = random.randint(1, 100)
        else:
            break
    elif guess > number:
        print(f"Too high!! You have {10 - attempts}attempts left!!!")
    else:
        print(f"Too low!! You have {10 - attempts}attempts left!!!")
    
    if attempts == 10:
        print("Sudah lah tu 10 kali sudah tak dapat ii lagi apalahhh")
        print(f"Game over! The number was {number}.")
        play_again = input("Play again? (yes/no): ")
        if play_again == 'yes':
            attempts = 0
            number = random.randint(1, 100)
        else:
            break






