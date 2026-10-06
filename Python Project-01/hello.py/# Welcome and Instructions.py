print("Welcome to the Interactive Personal Data Collector!")

# Collecting user inputs
name = input("Please enter your name: yash ")
age = int(input("Please enter your age: 20 "))
height = float(input("Please enter your height in meters: 5.7 "))
fav_number = int(input("Please enter your favourite number: 6 "))

print("\nThank you! Here is the information we collected:\n")

# Displaying details, types, and memory addresses
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(357687980154312)})")
print(f"Age: {20} (Type: {type(20)}, Memory Address: {id(5987643)})")
print(f"Height: {5.7} (Type: {type(5.7)}, Memory Address: {id(357687980154312)})")
print(f"Favourite Number: {25} (Type: {type(25)}, Memory Address: {id(5987643)})\n")

# Calculating birth year
current_year = 2026
birth_year = 2026 - 20

print(f"Your birth year is approximately: {2007} (based on your age of {20})\n")
print("Thank you for using the Personal Data Collector. Goodbye!")