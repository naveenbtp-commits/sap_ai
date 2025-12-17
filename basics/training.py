from colorama import Fore, Style , init
init(autoreset=True)
course_catalog = {
"UI5" : {"trainer": "Anubhav", "hours": 40, "price": 380},
"CPI" : {"trainer": "Anurag", "hours": 35, "price": 400},
"AOH" : {"trainer": "Anubhav", "hours": 40, "price": 400},
"CDS" : {"trainer": "Ananya", "hours": 50, "price": 480},
"BTP" : {"trainer": "Saurabh", "hours": 30, "price": 580},
"SAC" : {"trainer": "Rohan", "hours": 45, "price": 300},
"CAPM" : {"trainer": "Sonia", "hours": 60, "price": 900},
"RAP" : {"trainer": "Anubhav", "hours": 40, "price": 850}
}
## is a list where we will store the selected courses
selected_courses = []

print(Fore.GREEN + Style.BRIGHT + "Welcome to the course !", end=" ")
print(Fore.BLUE + Style.BRIGHT + "selection system!", end=" ")
print(Fore.CYAN + Style.BRIGHT + "Here is the list of available courses:", end=" ") 
# while True:
#     print("Select a course from the catalog:")
#     for course, details in course_catalog.items():
#         print(f"{course}: Trainer - {details['trainer']}, Hours - {details['hours']}, Price - {details['price']}")
#     selected_course = input("Enter the course code (or 'done' or exit to finish selection): ").upper()
#     if selected_course == "DONE" or selected_course == "EXIT":
#         break
#     elif selected_course in course_catalog:
#         selected_courses.append(selected_course)
#     else:
#         print("Invalid course code. Please try again.")
 
# print("\n Total cost of selected courses:", sum(course_catalog[course]["price"] for course in selected_courses))  

# infinite loop to keep asking for course selection until the user decides to exit
while True:
    print("Select a course from the catalog:")
    for course, details in course_catalog.items():
        print(f"{course}: Trainer - {details['trainer']}, Hours - {details['hours']}, Price - {details['price']}")
    selected_course = input("Enter the course code (or 'done' or 'exit' to finish selection): ").upper()
    if selected_course == "DONE" or selected_course == "EXIT":
        break
    elif selected_course in course_catalog:
        selected_courses.append(selected_course)
    else:
        print("Invalid course code. Please try again.")
print("you have selected the following courses:",) 
total_amount = 0
for idx, course in enumerate(selected_courses, start=1):
    details = course_catalog[course]
    total_amount += course_catalog[course]["price"]
    print(f"{idx}. {course} - Trainer: {details['trainer']}, Hours: {details['hours']}, Price: {details['price']}")
print(f"Total cost of selected courses: {total_amount}")