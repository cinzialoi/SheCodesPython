letters = ["a", "b", "c"]

#last week we saw how to print elements in a list one by one
#however to perform a task multiple times we use loops

# 2 types of loops
# while loops
#count = 0
# while 5 > count:
#     print('Hello')
#     count = count + 1

# name = input("What is your name? ")
# while name != "Ashley":
#     print("I don't know you!")
#     name = input("What is your name? ")

# 2nd type of loop
# For loops
# for letter in letters:
#     print(letter) #imagine we have created a variable called letter = 'a'
    # but we haven't! Python knows that I'm referring to the element in the list
    #THAT'S CRAZY

# #this below prints something 10 times
# for number in range (10):
#     print(number)

#it's the same as
#for number in range (0,10)
#which is similar to slicing

# students  = [
#     ["Cindy", "Emily", "Eve"],
#     ["Julie", "Maddy", "Andrea"],
#     ["Jenny", "Sarah", "Yara"]
# ]

# for student in students:
#     for name in student:
#         print(name)

#Exercises

# #Q1Ask the user for a number. Use a for loop to print the times tables for that number,up to ten
# number = input("Give me a number")
# count = 1
# while count < 11:
#     print (f"{number} x {count} = {int(number)*count}")
#     count += 1

#Q1Continuously ask the user to enter a number until they provide a blank input. Outputthe sum of all the numbers.
# number = input("Give me a number")
# sum = 0
# while number:
#     sum = sum + int(number)
#     number = input("Give me a number")
# print(sum)

#Ask the user to enter a in integer number. Print all the odd numbers between 0 andthat number (inclusive). (Its ok not to worry about negative numbers for now, unlessyou really want a challenge.)InputOutput9Enter a number: 9135whileTrue:# Do stuffwhileFalse# Doesn't matter what I put here - it'll never get run... :(
# number = int(input("Give me a number"))
# count = 0
# #list_of_numbers = []
# while count < number:
#     #list_of_numbers.append(count)
#     if count % 2 == 1:
#         print(count)
#     count += 1
#print(list_of_numbers[0:number:2])

#Write a guessing game.Select a number, and save it as a variable in your code. Ask the user to enter anumber, and then output whether their number is less than or greater than theselected number. Keep asking until the user guesses the correct number. Then print acongratulatatory message
# number = 84
# print("Guess the random number!")
# guess = int(input("Make a guess: "))
# while number != guess:
#     if guess < number:
#         print("Too low..")
#     else: 
#         print("Too high...")
#     guess = int(input("Make a guess: "))
# print("You got it right!")


#Q1Ask the user for a number. Use a for loop to print the times tables for that number,up to ten
# given = input("Give me a number")
# for number in range (1,11):
#     print (f"{given} x {number} = {int(given)*number}")

#Ask the user for an integer. Using a for loop, add up every number from 0 up to thatinteger, and print the result.
# given_number = int(input("Give me a number"))
# sum = 0
# for given in range (0,given_number+1):
#     sum = sum + given
# print(sum)

#