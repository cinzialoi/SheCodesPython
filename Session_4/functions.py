# #Function - an activity that is natural to OR the function of a person or thing
# # Function we've already seen:
# # input()
# # len()
# # print()
# # int()

# # name = input("What is your name? ")
# # age = input("How old are you? ")
# # if age >= 18:
# #     print("Welcome")
# # else:
# #     print("You cannot enter ")

# # If I have to ask a bunch of people the above, I can
# #simply create a function to store this, then I simply
# #have to call the function without repeating the code

# #task separation!

# def ask_user_name():
#     name = input("What is your name? ")

# def ask_user_age():
#     age = input("How old are you? ")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("You cannot enter ")

# #above we have defined 2 functions, and we can then call them
# #whenever we need

# ask_user_name()

# #Returning - if a function is returning something
# #it means is calculating and givng you something back
# #that you can capture

# def ask_user_name():
#     name = input("What is your name? ")
#     return name

# #return function immediately stops the execution of the rest 
# #of the code in the function


# #Parameters AKA Arguments
# total - 0 # --> Global variable IE variable that exists
# #and is accessible everywhere
# def add(number1, number2):
#     result = number1 + number2
#     return result

# answer = add(2,3)
# print(answer)
# print(result) # --> Local variable IE variable that exist
# #only inside of the function


#Write a function called get_integer that takes a string as its argument, and uses thatstring to prompt the user to enter an integer. Your function should return the integersupplied by the user.
# prompt ="Could I please have an integer?: "
# # Define your function here
# def get_integer(number):
#     user_input = int(input(prompt))
#     return user_input
# user_input = get_integer(prompt)
# print(f"So your integer is {user_input}? Thanks!")

#Write a function called celcius_convert that takes a number representing thetemperature in Farenheit as its argument, and returns a float representing thetemperature in Celcius
# degrees_f = 350 # Assign some number as the value here
# # Define your function here
# def celcius_convert(farenheight):
#     celcius = (farenheight - 32) * 5/9
#     return celcius
# print(celcius_convert(degrees_f))


#Write a function that accepts one argument (an integer) and returns True when thatargument is odd and False when that argument is even. You can use the same formatas the starter code in the previous exercise. Just remember - you're returning theresult, not printing it!
# def odd(number):
#     if number%2 == 1:
#         value = True
#     else:
#         value = False
#     return value
# is_it_odd = odd(5)
# print(is_it_odd)

#Write a function that takes two arguments; the unit price of an item, and how manyunits were purchased. Return the total cost as a string.
def item_total(price_per_unit, num_units):
    tot = price_per_unit * num_units
    return str(tot)
strawberries = item_total(3.45, 5)
print(strawberries)