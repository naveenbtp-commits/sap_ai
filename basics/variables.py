# # Variable assignment and basic operations
# name = "Alice"
# age = 25
# height = 5.8
# is_student = True

# # Display variables
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Height: {height}")
# print(f"Is Student: {is_student}")

# # Variable operations
# birth_year = 2024 - age
# print(f"Birth Year: {birth_year}")

# # Multiple assignment
# x, y, z = 10, 20, 30
# print(f"x={x}, y={y}, z={z}")

# # Type checking
# print(f"Type of name: {type(name)}")
# print(f"Type of age: {type(age)}")
# is_student = False

# print("is_student is of type ", type(is_student))
import datetime


newage = input("Enter your age: ")
# print("Your age is: ", newage)
print(f"current time is {datetime.datetime.now().strftime('%H:%M:%S')}")
if int(newage) > 18:
    print("You are an adult.")
elif int(newage) == 18:
    print("You are exactly 18.")
else:
    print("You are a minor.")