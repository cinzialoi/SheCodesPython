# #if you want to store multiple bits of data you create lists
# list_name = []

# #list can take different data types, and each element is separated by a comma:
# list_name = ["asli",1,4.5,[]]

# #although it makes sense to group same data types together
# #you can group different types of data if the occasion calls for it

# #lists are index based which starts from 0
# digits = [0,1,2,3,4,5]
# # the . below is called "method" - it calls certain functions that are pre-written
# digits.append

# #to extract the first element from your list
# print(digits[0])

# #to check the last element 
# print(digits[-1])

# #to check second last element
# print(digits[-2])

# #to print specific elements "slicing" a list. 
# #start is only includive and end is alwys exclusive
# print(digits[0:4])

# #to print the last part of the list (given that end is exclusive) 
# print(digits[4:])

# #the last element tells it to print every single 1
# print(digits[0:6:1])

# #the last element tells it to print every 2nd one
# print(digits[0:6:2])

# # to know how many elements in a list
# print(len(digits))

# #to add something at the end of the list
# digits.append(6)

# #to takes the index you're specifying and removes it and returns it from the list
# digits.pop() #if left empty it defaults to -1

# #"return" when something returns something it can be captured and stored

# #replace the index with a different value
# digits[3] = 90

#nested lists IE a list within a list
# letters = ["a","b","c","d",["Emily","Julie","Cinzia"]]
# print(letters[4][0])

# #to check if an element is in a list
# if "A" in letters:
#     print("it's in the list")
# else:
#     print("it's not here, try again")


#Exercises

#Given the list of foods below, print:The first item in the list.The third item in the list.The last item in the list.The first three items in the list.The last three items in the list.The last item in the sublist
# foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[-3:])
# print(foods[6][-1])

#Format and print the contents of the following list so that the output appears asdepicted
number_5 =[["Monica", "in my life"],["Erica", "by my side"],["Rita's", "all I need"],["Tina's", "what I see"],["Sandra", "in the sun"],["Mary", "having fun"],["Jessica", "here I am"]]
#print(number_5)
#number_5.insert([]["A little bit of"])

#print(number_5[0][0:2])

# print("A little bit of", number_5[0][0], number_5[0][1])
# print("A little bit of", number_5[1][0], number_5[1][1])
# print("A little bit of", number_5[2][0], number_5[2][1])
# print("A little bit of", number_5[3][0], number_5[3][1])
# print("A little bit of", number_5[4][0], number_5[4][1])
# print("A little bit of", number_5[5][0], number_5[5][1])
# print("A little bit of", number_5[6][0], number_5[6][1])
# print("A little bit of you makes me your man (ah!)")
# print("*trumpet solo*")


#Ask the user for three names. Add each name to a list, and then print the list.
# first_target = input("Tell me who's the first person we're targeting: ")
# second_target = input("Who's the second? ")
# third_target = input("What about the third? ")
# hitmanlist=[first_target,second_target,third_target]
# print(hitmanlist)

#Using the following starter code:
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = []
e = []

#Print the following lists:
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]][1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = [a,b,c,[a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2]]]
print(new_list)