# mylist_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# mylist_numbers = [1, 2, 3, 4, 5]

# print("first item", mylist_fruits[0])  # Output: apple    
# print("last item", mylist_fruits[4])  # Output: elderberry
# mylist_fruits.append('fig')  # Add 'fig' to the end of the list
# print("updated list", mylist_fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
# mylist_fruits.remove('banana')  # Remove 'banana' from the list
# print("updated list", mylist_fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry', 'fig']
# mylist_fruits.pop()  # Remove item at index 2
# print("updated list", mylist_fruits)  # Output: ['apple', 'cherry', 'elderberry', 'fig']
# mylist_fruits.insert(3, 'grape')  # Insert 'grape' at index 3
# print("print in middle list", mylist_fruits[2:4])  # Output: ['date', 'elderberry']
# print("print in middle list", mylist_fruits[2:-1])  # Output: ['date', 'elderberry']
# print('number of items in list', len(mylist_fruits))  # Output: 6

# if 'cherry' in mylist_fruits:
#     print("cherry is in the list")  # Output: cherry is in the list
#     new_list = mylist_fruits+mylist_numbers
#     print("combined list", new_list)  # Output: ['apple', 'cherry', 'date', 'elderberry', 'fig', 'grape', 1, 2, 3, 4, 5]
#     squared_list = [x**2 for x in mylist_numbers]
#     print("squared list", squared_list)  # Output: [1, 4, 9, 16, 25]

###Example of sets
# Sets are unordered collections of unique elements
# # Example of creating a set
# my_set = {1, 2, 3, 4, 5}
# # Adding elements to a set
# my_set.add(6)
# # Removing elements from a set
# my_set.remove(2)
# # Checking membership in a set
# if 3 in my_set:
# 	print("3 is in the set")
# # Set operations
# union_set = my_set.union({7, 8})
# intersection_set = my_set.intersection({3, 4, 5})
# print("intersection_set:", intersection_set)
# # Printing the results
# print("Union of sets:", union_set)
# tuple of tuples examples 
# mytuple = (1, 2, 3, 4, 5)
# print("Tuple:", mytuple)
# print("First item in tuple:", mytuple[0])
# print("Last item in tuple:", mytuple[-1])
# print("Number of items in tuple:", len(mytuple))
# a, b, c, d, e = mytuple
# print("Unpacked tuple:", a, b, c, d, e)
# nested_tuple = ((1, 2), (3, 4))
# print("Nested tuple:", nested_tuple)
# a, b = nested_tuple
# print("Unpacked nested tuple:", a, b)

##Dictionaries
# Dictionaries are collections of key-value pairs like JSON objects
# Example of creating a dictionary of employee data
employee_data = {
"name": "John Doe",
"age": 30,
"department": "Engineering",
"skills": ["Python", "JavaScript", "C++"]
}
print("Employee data:", employee_data)
print("Employee name:", employee_data["name"])
print("Employee department:", employee_data.get("age", "Unknown"))
# print("Employee age:", employee_data.pop("age"))
print("Employee department:", employee_data.get("age", "Unknown"))
print("Employee data:", employee_data)
for key, value in employee_data.items():
    print(f"{key}: {value}")    # Output: name: John Doe, age: 30, department: Engineering, skills: ['Python', 'JavaScript', 'C++']
del employee_data["skills"]
print("Employee data after deletion:", employee_data)    