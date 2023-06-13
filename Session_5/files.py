#to call file you use the open function
#parameters can be given in different order but must be called by their name
#this is a variable. You can use this to refer to that file
#if you use default, you can simply give it a file name
import csv

# with open(file="dogs.csv", mode ="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)


#to create file you change the mode to w = write
with open(file="hell0.csv", mode ="w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(["this is a string", "Hi"])

#to add data to a list
population = []
with open("hell0") as Gibberish:
    csv_reader = csv.reader(Gibberish)
    for line in csv_reader:
        population.append(line)

# print(population)


