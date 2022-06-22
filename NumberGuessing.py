import random

range = input("Type the range of numbers, example, the range goes from 0 to 10 type 0 10 \n"
        "None of the numbers can be negative: ")
# Create a list in which will be saved the numbers inputed by the user
range_list = [range]

# Iterate trough the values of the list and split the 2 numbers inputed by the user
for index, value in enumerate(range_list):
    new_list = value.split(" ")
    # If the input is not a number quit the program
    try:
        random_number = random.randint(int(new_list[0]), int(new_list[1]))
    except ValueError:
        print("You didn't type a number followed by a space and another number, \n"
        "or you typed a negative number. Try again...")
        quit()
    # If the first number is the same as the second number quit the program
    if int(new_list[0]) == int(new_list[1]):
        print("The second number needs to be bigger than the first number. Try again...")
        quit()
    # If the first number is negative quit the program
    elif int(new_list[0]) < 0:
        print("The numbers can't be negative. Try again...")
        quit()

number_of_guesses = 0

while True:
    user_guess = input("Try to guess the number generated randomly: ")
    # If the inputed number is a digit increment number of guesses
    if user_guess.isdigit():
        user_guess = int(user_guess)
        number_of_guesses += 1
    # If the number is not a digit quit the program
    else:
        print("You have to guess a number!! Try again...")
        quit()
    # If the user guesses the number print win
    if user_guess == random_number:
        if number_of_guesses == 1:
            print("WOW, you guessed the number in", number_of_guesses, "guess!!")
        if number_of_guesses >= 2 and number_of_guesses < 10:
            print("Congratulations, you guessed the number in", number_of_guesses, "guesses!")
        if number_of_guesses >= 10:
            print("You guessed the number in", number_of_guesses, "guesses, " 
            "better luck next time.")
        break
    # If the number guessed is bigger than the number print above
    elif user_guess > random_number:
        print("You were above the number. Keep trying.")    
    # If the number guessed is smaller than the number print below
    else:
        print("You were below the number. Keep trying.")