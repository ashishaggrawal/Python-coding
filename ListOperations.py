# # working with lists

# # loops

# cars = ["Tesla", "Hyundai", "Toyota", "Tata", "Honda", "Audi"]
# print(cars)

# for car in cars:
#     #for loop help us in printing the elements in rhe list without repeating print statement.
#    #for loop will ask list cars to align all elements in the list to car variable. then loop will print them
#    # print(car[2])  this coomand will print string at index 2 of all elements of the list. It wont print 2nd element of the list which is "Toyota"
    
#     print(f"{car.upper()} is an amazing car")
#     print(f"Cant wait to buuy my new {car.upper()}\n")

# # range function in loops

# for value in range(1,10):
#     print(f"Value is {value}")

# # using range numbers to create a list of numbers
# number = list(range(1,6))
# print(number)

# even_number = list(range(2,11,2)) # start with 2 till 11(not included) with the gaps of 2
# print(even_number)

# ######### very important ##############
# We can create a new set of list s using range() function. 

number = []
for num in range(4, 20, 2):
    square = num ** 2
    number.append(square)
    
print(number)
print(min(number))
print(sum(number))

#list comprehesion
square = [value **2 for value in range(1,11)]
print(square)

# Comparison Summary

# Feature                  Syntax Placement                 Example
# ###################################################################################################
# Basic                 [expr for item in list]         [x*x for x in nums]
# Filtering             At the end                      [x for x in nums if x > 0]
# If/Else               At the start                   [x if x > 0 else 0 for x in nums]

numbers = [1,2,3,4,5]
new_numbers = [p*10 for p in numbers]
print(new_numbers)

ages = [12, 21, 15, 30, 17, 45]
new_age = [n for n in ages if n>=18]
print(new_age)


files = ["Vacation.jpg", "Notes.txt", "Selfie.JPG", "Budget.xlsx"]

# Correct comprehension:
new_files = [x.lower() for x in files if x.lower().endswith(".jpg")]
print(new_files)

raw_emails = ["  Alice@Gmail.com", " ", "bob@yahoo.com  ", "invalid-email", "CHRIS@outlook.com"]
new_email = [x.strip().lower() for x in raw_emails if "@"in x]
print(new_email)












