#Boolean
#name = 'Cinzia'
#age = 29
#height = 1.61
#is_raining = True
#my_variable2 = False
#print (is_raining)
#print(type(is_raining))

#boolean expression - Expressions that produce a boolean valie 
# comparison operators
# == checks if what we are comparing is equal
# != checks if something is not equal to somethingselse
# > (greater than) < (Less than) >= and <=
#print(5 > 3)

#Matematical Operators - Addition, division subtractions etc
#Boolean operators - not, and, or
is_sunny = True
is_warm = True

#print(not is_sunny)
#print (is_sunny and is_warm)
#print (whether) (is_sunny or is_warm) (is true)

#conditional
# syntax (the grammar) vs semantics (the logic)
#temperature = 17
#if temperature < 18:
#    print("weather is too cold!")
#elif temperature > 28:
#    print("weather is too hot!")
#else:
#    print ("weather is nice!")
#print("my dog looks cute")

#multiple if statements, it will check the expression truthness regardless
#in order you must use if, elif, else

#Excercises
# Sara is a confident rock climber, but sometimes she forgets her helmet. Rei refuses toclimb with Sara unless she's wearing a helmet, because That's Just Sensible.Write a program that sets the value for a boolean variable called sara_has_helmet, andthen prints out a string indicating whether or not Rei is down to climb.

sara_has_helmet = False
#if sara_has_helmet:
#    print("Let's send it!")
#else:
#    print("No way, my brain is my moneymaker!")

#Rei is a very careful climber, but sometimes she is forgetful. Even if Sara has a helmet,they still can't go climbing unless Rei remembers to bring her rope.Amend the previous program to add a check for the rope before you output the result
# rei_has_rope = False
# if (sara_has_helmet and rei_has_rope) :
#     print("Let's send it!")
# elif (sara_has_helmet and not rei_has_rope):
#     print("Who's unprepared now, Rei??")
# elif (not sara_has_helmet and rei_has_rope):
#     print("No way, my brain is my moneymaker!")
# else:
#     print("I guess let's just go hiking?")

#Write a program that implements the algorithm for red light cameras. The programshould print the string "Flash!" if (and only if) a car is detected driving while the lightis red. If the light is green or amber, the program should print "Do nothing.", evenwhen a car is detected
# light_color = "Green"
# car_detected=True

# if (light_color == "Red" and car_detected):
#     print("Flash!")
# else:
#     print("Do nothing!")

#Write a program that asks the user for their height, and determines whether or notthey are tall enough to ride the rollercoaster, which has a height requirement of120cms.
# height = int(input("How tall are you in cm "))
# if height >= 120:
#     print("Hop on!")
# else:
#     print("Not today!")

# Write a program that asks the user to enter their username and password and output asuccess message if they are correct, or a failure message if they are incorrect. Yourprogram has one user, whose username is "lucyg", and whose password is "quartzgleam?1"
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if (username == "lucyg" and password == "quartzgleam?1"):
#     print("Logged in successfully.")
# else:
#     print("Access Denied")

#Write a program that asks the user to enter their email address and checks whether itis valid or not. For the purpose of this exercise, you can make the assumption that anemail address is valid if it contains a “@” symbol and a “.” symbol
# email = input("Verify your email: ")
# if ("@" in email):
#     print("Email valid")
# else:
#     print("Invalid email detected!")

    #
if "False":
    print("A strange game. The only winning move is not to play.")