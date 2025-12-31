# List in python
print("Python: Lists")
cars = ["Tesla", "Hyundai", "Toyota", "Tata", "Honda", "Audi"]
print(cars)

# # Accessing Elemnets in the list
# # Provide postion or index number of the desired item. index numbers start from 0

# print(f"I have {cars[1]}.")
# print(f"I want to buy {cars[4]}")
# print(f"but can effort only {cars[-4]}")

# # Modifying elements in a list
# cars[2] = "BMW"
# print(cars)

# # Adding elements to the list
# cars.append("Volvo")
# print(cars)

# #Inserting elements to the list at a specific position
# cars.insert(3, "kia")
# print(cars)

# #Removing elements from a list
# del cars[3]
# print(cars)

# #Removing elements using pop() method. It removes last item from the list.
# print(cars.pop()) # print the element that has been popped.
# print(cars)

# #popped out an element from any postion.
# print(f"my last car was {cars.pop(2).lower()}")

# #remove a item by value
# cars.remove("Audi") #it we print this statement None will be printed. 
# print(cars)

# #We can assigne an item to a variable and then use that variable name to remove it.
# too_expensive = "Tesla"
# cars.remove(too_expensive)
# print(f"{too_expensive.upper()} is too expensive so removing from the list. No I have {cars} in my wishlist ")

cars.append("Volvo")
cars.append("Tesla")
cars.append("BMW")
# print(cars)

# #Sorting the list items permanently
# cars.sort()
# print(cars)

# #Sorting the list items but in reverse
# cars.sort(reverse=True)
# print(cars)

#Temporary sort- it maintains original order of the list

print(f"After sort:{sorted(cars)}")
print("--------------------")
print(f"Original: {cars}")

#finding the lenght of the list
print(len(cars))