import random
top_of_range=int(input("Type a number: "))
if top_of_range<=0:
    print("Please enter a valid number")
    quit()

random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess=int(input("...Make a guess..."))
    if user_guess == random_number:
        print("Your got it !!")
        break
    elif user_guess>random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print("The number of guesses done is ",guesses)
    
