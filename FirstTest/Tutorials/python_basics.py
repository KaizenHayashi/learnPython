print("Ayo wassap\n")

print("   /|")
print("  / |")
print(" /  |")
print("/___|\n")

character_name = "Kiieta"
character_age = "15"
print("Once upon a time there was someone named " + character_name + ",")
print("They were " + character_age + " years old.")

character_name = "Kizaru"
print("They really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".\n")

print("Use the syntax r\"\\\" to use a backslash as raw text.")
print(r"test \ test")
print("Otherwise, just use \"\\\\\"\n")

print("--------------------------------------------------------------------------\n")

phrase = "This entire section is"

print(phrase + " appending another string called \"concatenation\".\n")

print(phrase.lower() + " converting the phrase to lower case.")
print(phrase.upper() + " converting the phrase to upper case.\n")

# Use str() to convert variables into string.
print(phrase + " for checking if the phrase is fully lower or upper case. Which is \"" + str(phrase.isupper()) + "\".")
print(phrase + " for checking the length of the phrase. Which is \"" + str(len(phrase)) + "\" characters.\n")

# Python counts the first character as the 0th index.
print(phrase + "for checking the position/index of a character in a given phrase.\nThese two examples are for the "
               "letter \"r\".")
# You can put in words or phrases instead of letters to see where the matched case starts.
print("The letter \"r\" is at the " + str(phrase.index("r")) + "th index.")
print("The 9th index is the letter \"" + phrase[9] + "\".\n")

print(phrase.replace("entire section", "whole part") + " for replacing parts of a string during printing.")

print("--------------------------------------------------------------------------\n")

print(5.57423 - 88.45612)
print(2 * 2 + 3)
print((2 * 2) + 3)
print(2 * (2 + 3))
print()

print(10 % 3)
print("This \"%\" sign means \"modulus\".")
print()

print(abs(-874536))
print(round(-5.49, 1))
print(max(1, 2))
print(min(1, 2))
print()

print(pow(2, 3))
print(2 ** 3)
print()

print(4 ^ 4)
print("I have no clue what \"^\" does yet.\n")

from math import *

print(ceil(4.1))
print(floor(4.1))
print(sqrt(4.1))

print("--------------------------------------------------------------------------\n")

number = input("Enter your social security number: ")
age = input("Enter your age: ")
print("Your account " + number + " is now compromised. you are a stupid " + age + " years old.\n")

# Calculator v1.0
numc1 = input("Enter a number: ")
numc2 = input("Enter another number: ")
result = float(numc1) + float(numc2)
print(result)
print()

colour = input("Enter a colour: ")
plural_noun = input("Enter a plural noun: ")
food = input("Enter a food: ")

print("Roses are " + colour)
print(plural_noun + " are blue")
print("I love " + food)

print("--------------------------------------------------------------------------\n")

liste = ["Keiko", False, 3.142, "Zen", "Kai"]
liste[1] = True
print(liste[1])
print(liste[3:])
print()

fibonacci_0 = [1, 2, 3, 5, 8, 13, 21]
humans_0 = ["Amanda", "Brian", "Callista", "Darren", "Emily"]
fibonacci_0.extend(humans_0)
print(fibonacci_0)
print()

fibonacci_1 = [1, 2, 3, 5, 8, 13, 21]
fibonacci_1.append(34)
print(fibonacci_1)
print()

humans_2 = ["Amanda", "Brian", "Callista", "Darren", "Emily"]
humans_2.insert(2, "Yorgo")
print(humans_2)
print()

fibonacci_3 = [1, 2, 3, 5, 8, 13, 21]
fibonacci_3.pop()
print()

humans_4 = ["Amanda", "Brian", "Callista", "Darren", "Emily"]
humans_4.remove("Darren")
print(humans_4)
print()

fibonacci_5 = [1, 2, 3, 5, 8, 13, 21]
fibonacci_5.clear()
print(fibonacci_5)
print()

# Index function only shows the first appearance.
fibonacci_6 = [1, 2, 3, 5, 8, 13, 21, 13, 34, 13]
print(fibonacci_6.index(13))
print(fibonacci_6.count(13))
print()

fibonacci_7 = [1, 2, 3, 5, 8, 13, 21, 13, 34, 13]
fibonacci_7.sort()
print(fibonacci_7)
print()

fibonacci_8 = [1, 2, 3, 5, 8, 13, 21]
fibonacci_8.reverse()
print(fibonacci_8)
fibonacci_9 = fibonacci_8.copy()
fibonacci_9.append(69)
print(fibonacci_9)
print()

print("This is a tuple. It's just an immutable list.")
coordinates = (1, 2, 3)
print(coordinates[1])
print()

print("--------------------------------------------------------------------------\n")


def say_hi():
    print("Hello World")


say_hi()
print()


def say_hello(name, foodstuff):
    print("Hello " + name + ", you like to eat " + foodstuff + ".")


say_hello("Maki", "cake")
say_hello("Raven", "watermelons")
print()


def cube(numm):
    return numm * numm * numm


print(cube(4))

resultt = cube(4)
print(resultt)
print()

print("--------------------------------------------------------------------------\n")

is_left = True
is_up = False
if is_left and is_up:
    print("It's left and up.")
elif is_left and not is_up:
    print("It's left but not up.")
elif not is_left and is_up:
    print("It's not left but it's up.")
else:
    print("It's not left and not up.")
print()


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(1, 2, 3))
print()


def same_num(numa1, numa2):
    if numa1 != numa2:
        return str(numa1) + " is not " + str(numa2) + "."
    else:
        return str(numa1) + " is the same as " + str(numa2) + "."


print(same_num(1, 2))
print()

# Calculator v2.0
numb1 = float(input("Enter a number: "))
op = (input("Enter operator sign: "))
numb2 = float(input("Enter another number: "))

if op == "+":
    print(numb1 + numb2)
elif op == "-":
    print(numb1 - numb2)
elif op == "*":
    print(numb1 * numb2)
elif op == "/":
    print(numb1 / numb2)
else:
    print("Invalid operator.")

print("--------------------------------------------------------------------------\n")

# Keys
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    11: "November",
    12: "December"
}

print(monthConversions["Mar"])
print(monthConversions.get("Luv", "Not a valid Key."))

# += is the same as [variable] + 1.
jonga = 1
while jonga < 7:
    print(jonga)
    jonga += 1
else:
    print("Done")
    print(jonga)

print("--------------------------------------------------------------------------\n")

secret_word = "secret"
guess = ""
guess_try = 0

while guess_try < 3:
    if guess != secret_word:
        guess = input("Enter guess: ")
        guess_try += 1
        if guess == secret_word:
            print("You win!\n")
if guess != secret_word:
    print("You lose!\n")

secret_word = "secret"
guess = ""
guess_try = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_try < guess_limit:
        guess = input("Enter guess: ")
        guess_try += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!\n")
else:
    print("You win!\n")

print("--------------------------------------------------------------------------\n")

for letterr in "Kaizen":
    print(letterr)
print("\n")

people = ["Abraham", "Banana", "Catto"]
for namee in people:
    print(namee)
print("\n")

for indexx in range(3, 10):
    print(indexx)
print("\n")

for indexxx in range(5):
    if indexxx == 1:
        print("second iteration")
    else:
        print("not second iteration")
print("\n")

print("--------------------------------------------------------------------------\n")


def raise_to_power(base_num, power_num):
    resulttt = 1
    for indexxxx in range(power_num):
        resulttt = resulttt * base_num
    return resulttt


print(raise_to_power(4, 6))
print(4**6)

print("--------------------------------------------------------------------------\n")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["#", 0, "*"]
]

print(number_grid[0][0])
print(number_grid[1][2])
print(number_grid[2][1])
print(number_grid[3][2])
print("\n")

for row in number_grid:
    print(row)
    for col in row:
        print(col)
    print("\n")


def translate(pphrase):
    translation = ""
    for letterrr in pphrase:
        if letterrr.lower() in "aeiou":
            if letterrr.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letterrr
    return translation


print(translate(input("Enter a phrase: ")))

print("--------------------------------------------------------------------------\n")

try:
    numnum = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

print("--------------------------------------------------------------------------\n")

# "r" for read only, "r+" for read and write
# "w" for write
# "a" append/add only
examples_file = open("examples.txt", "r")

# If this file is readable
print(examples_file.readable())
print()

# Reads individual lines
# (n) controls the number of characters showing up
# [n] controls the line of the item in the file
print(examples_file.readline())
print(examples_file.readline())
print(examples_file.readline(9))
print()

# Reads at where it was last left unread
print(examples_file.readlines()[1])

# Reads entire file
print(examples_file.read())
print()

examples_file.close()

examples_file = open("examples.txt", "r")
for example in examples_file.readlines():
    print(example)
examples_file.close()

examples_file.close()

examples_file = open("examples.txt", "a")

# This code runs every time you run the code so be careful.
##examples_file.write("\nAngo - sister")

examples_file.close()

# You can use the "open" function to create a new file.
##examples_file = open("emxamples.txt", "w")

print("--------------------------------------------------------------------------\n")

import basic_tools

# Get official Python modules online
print(basic_tools.roll_dice(6))
print()

# pip install python-docx qwertyuiop[]
# Use "pip" in cmd to install some modules online.

from basic_tools import Student

student1 = Student("Jire", "Business", 3.1, False)
student2 = Student("Boh", "Art", 2.9, True)

print(student1.name)
print(student1.gpa)
print()
print(student2.major)
print(student2.is_on_probation)
print()
print(student1.on_honour_roll())
print(student2.on_honour_roll())
print()

print("--------------------------------------------------------------------------\n")

question_prompts = [
    "What colour are oranges?\n(a) Orange\n(b) Lemon\n(c) Blue\n\n",
    "What comes after 2?\n(a) 3\n(b) 4\n(c) 438765\n\n",
    "What is the first letter of the alphabet?\n(a) A\n(b) B\n(c) C\n\n"
]

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) + " questions right!")

run_test(questions)

print("--------------------------------------------------------------------------\n")

from basic_tools import Chef

myChef = Chef()
myChef.make_pasta()

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice.\n")

print("--------------------------------------------------------------------------\n")

print("The end :D")