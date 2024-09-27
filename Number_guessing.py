import random
easy_level_turns=5
hard_level_turns=10

def check_answer(guess,number):
    if guess<number:
        print("Too high")
    elif guess>number:
        print("Too low")
    else:
        print(f"You are rigth, the correct answer is {number}")

def diff():
    difficulty=(input("Choose the difficulty.Type 'easy' or 'hard' :"))
    if difficulty=="easy":
            return easy_level_turns
    elif difficulty=="hard":
            return hard_level_turns
            

logo=''''''''''
  ___  __ __    ___  _____ _____      ____   ____  ___ ___    ___ 
 /    ||  |  |  /  _]/ ___// ___/     /    | /    ||   |   |  /  _]
|   __||  |  | /  [_(   \_(   \_     |   __||  o  || _   _ | /  [_ 
|  |  ||  |  ||    _]\__  |\__  |    |  |  ||     ||  \_/  ||    _]
|  |_ ||  :  ||   [_ /  \ |/  \ |    |  |_ ||  _  ||   |   ||   [_ 
|     ||     ||     |\    |\    |    |     ||  |  ||   |   ||     |
|___,_| \__,_||_____| \___| \___|    |___,_||__|__||___|___||_____| '''''''''
                                                                   
print(logo)

number=random.randint(1, 100)#Choose one number between parameters
print("Welcome to Guessing Game")
print("Gues a number between from 1 to 100")
diff()
guess=int(input("Make a guess"))
turns=diff()
print(f"Ypu have {turns} attempts remaining to guess the number")

