print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
numbers = []
def factors(num1):
    for i in range(1, num1+1):
        if num1 % i == 0:
            numbers.append(i)
    return numbers

print(factors(12))

# A1a:



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def is_factor (num1,num2):
    if num1 % num2 ==0 or num2 % num1 ==0:
        return True
    else:
        return False
print(is_factor(2,16))
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def pos (letter = "f"):
    if letter in alphabet:
        return alphabet.index(letter) + 1

print(pos("z"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def name_id (name= "bob"):
    code = []
    for i in name:
        code.append(str(alphabet.index(i)))

    return(''.join(code))


print(name_id())


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password (num):
    count = 0
    for i in num:
        count += int(i)
    return int(num) - count

print(password(name_id()))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def prime(num= input("Enter a number ")):
    while num.isdigit() == False:
        num = input("Enter a number ")
    pr = True
    num=int(num)
    for i in range(2, num):
        if num % i == 0:
            pr = False
    if pr == False and num != 2:
        return False
    elif num == 1 or num == 0:
        return False
    else:
        return True

print(prime())

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #



