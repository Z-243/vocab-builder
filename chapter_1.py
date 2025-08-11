# HOW TO PRINT

# print('hello there')

listOfGroceries = ['eggs', 'apples', 'oranges']
# print(listOfGroceries[2])

student_data = {"name": "sam",
                "age": 15,
                "grade": {"math": "B",
                          "eng": "C",
                          "science": "A"}}

# print(student_data["grade"])


## LOGIC AND OPERATIONS
number_of_eggs = 2

if number_of_eggs > 6:
    print("You have more than 6 eggs")

if "activity" in student_data:
    print(student_data["activity"])
# else:
#     print("the key name is not available in the dictionary")

if "mangoes" in listOfGroceries:
    print("It is present")
# else:
#     print("It is not present")

## LOGICAL OPERATORS — and or

if number_of_eggs > 5 and number_of_eggs < 20:
    print("we more than 5 eggs but less than 20")

age = 23

if age >= 24 and age < 57:
    print("Within age limit of 24-57")


## OPERATORS

x = 5
y = 6
# print( x + y ** y * x - y / x)
# print(x % 2 == 1)

# print(x != y)

# if not age == 44:
#     print("age is not 44 but", age )
#     print(f"age is not 44 but, {age} ")

## LOOPS (while/ for)

count = 0
# while count < number_of_eggs:
#     print("hello")
#     count += 1
#     if count == 1:
#         break

# for x in listOfGroceries:
#     print(x)

# for y in student_data:
#      print(f" {y} -> {student_data[y]}")

# for i in range(4):
#     print(i)

length_of_array = len(listOfGroceries)

# for i in range(length_of_array):
#     current_index= i
#     current_value = listOfGroceries[i]
#     print(f'curent index is {current_index} and value is {current_value}')

## FUNCTIONS

def print_a_fun_word(fun_word):
    '''this is a function that takes an argument and prints that word'''
    print(fun_word)

# print_a_fun_word(input("enter a funny word... "))

def add_two_numbers(number1, number2):
    return number1 + number2

# addition = add_two_numbers(2, 4)
# print(addition)

## OOP

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print('oh hi there!')

new_person = People("don", 69)

new_person.greet()
print(new_person.name)

person_2 = People("Lucy", 55)
print(person_2.age)