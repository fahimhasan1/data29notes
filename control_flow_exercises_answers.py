print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
def numbers(list):
    print(list[:5])
numbers(x)
# A1a:

print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
def is_even(list):
    for num in list:
        if num % 2 == 0:
            print(num)
is_even(x)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
# for num in x[:5]:
#     if num % 2 == 0:
#         print(num)

def is_even_extra(list):
    for num in list[:5]:
        if num % 2 == 0:
            print(num)
is_even_extra(x)


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
name_letter=[]
# for name in names:
#     name_letter.append(name[0])
#
# print(name_letter)
def n_l(list):
    for name in list:
        name_letter.append(name[0])

n_l(names)
print(name_letter)
print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index=[]
for name in names:
    space_index.append(name.index(" "))
print(space_index)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
first_last = []
for name in names:
    first_last.append(name[0] + name[name.index(" ") + 1])

print(first_last)



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
for item in list_of_lists:
    #new_list = set(item)
    #print(new_list)
    if len(item) == len(set(item)):
        print(item)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
number = True
# while number:
#     user = input("\nEnter a number greater than 100 ")
#     try:
#         user_num = float(user)
#         if user_num < 100:
#             print("\nThis number is too low, try again ")
#         elif user_num > 100 :
#             print("Well done you know numbers " + str(user_num))
#             number = False
#         elif user_num == 100:
#             print("\nPlease enter a number BIGGER than 100, try again ")
#         else:
#             print ("Invalid input, try again ")
#     except ValueError:
#         print("Invalid input, try again ")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

prime = True
while number:
    user_num = int(input("\nEnter a whole number greater than 100 "))

    if user_num < 100:
        print("\nThis number is below 100, try again ")
    elif user_num > 100:
        print("Well done you know numbers.\n" + str(user_num))
        for i in range(2, user_num):
            if user_num % i == 0:
                prime = False
        number = False
    elif user_num == 100:
        print("\nPlease enter a number BIGGER than 100, try again. ")
    else:
        print ("Invalid input, try again ")

if prime == False:
    print("The number you have entered is not a prime number. ")
else:
    print("The number you have entered is also a prime number. ")
