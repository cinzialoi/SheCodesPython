# Creating variable and assigning Data to them. 
# Conventionally these are all lowercases and separated by underscores
first_name = "Asli"
last_name = "Loi"

#Data types - Text data, Numerical data
#Text data --> String
today = "Tuesday"
#print is a ~function~
print(today)
#print(f"Today is"{today}) #prints fixed value
print(type(today)) #prints (tells you) what the type of the variable is 

#numerial data types - Integer, Float 
# Integer - whole number
parkers_age = 4
print(type(parkers_age))
print(f"Parker is turning {parkers_age+1} soon!")
height = 161
print(f"My height is {height/100}m")

#decimal is called a float
weight = 73.4 
print(type(weight))
print(f"My weight is{weight*2.1}in lbs")

#below will return error because I'm trying to add an int to a string
distance = "5000"
#print(distance +8)
#however if I define the type of variable that I want to change it to it works
#int + int
print(int(distance)+8)
#str + str
print(distance +str(8))

#literally expects an input, the value in the quotes explains what input we're asking for
dog_name = input("What is your dog's name?")
print(f"Nice to meet you {dog_name}!")

birth_year = input("What year were you born?")
print(f"Oh! So you're {2023-birth_year}old")