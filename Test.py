import random
import sys
import os

print("hello")

# double quotes and single quotes does not really matter for python

# multiline comments
'''
sadfsadf
'''

## how to print
name2 = "Berkay"
print(name2)
num = 15
print(num)

# operations
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 ** 3 =", 5 ** 3)
print("5 // 2 =", 5 // 2)
# order is important (it works like real math)
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# string operations
quote = "\"Always remember you are unique\""
print(quote)

multi_line_quote = '''everything
something
happened
fatih terim'''
print(multi_line_quote)

print('\n' * 5)

print("%s%s    %s" % ('giris\n', quote, multi_line_quote))

####
print("I don't like ", end="")
print("newlines")

print("I don't like ", end="newlines")
print('\n' * 5)
####

long_string = "I'll catch you if you fall - The Floor"
## first 4 characters
print(long_string[0:4])
## last 5 characters
print(long_string[-5:])
## w/o last 5 characters
print(long_string[:-5])
## first 4 characters + " be there"
print(long_string[0:4] + " be there")
## c stands for character, s stands for string, d stands for decimal, f stands for fraction
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, .14))
## capitalize first character and unc. rest
long_string = "i'll catch you if you fall - The Floor"
long_string = long_string.capitalize()
print(long_string)
## index value of a start of a string - case sensitive
print(long_string.find("floor"))
## if all string is letters, true
print(long_string.isalpha())
## if all string is number, true
print(long_string.isalnum())
## replace one string with another
print(long_string.replace("floor", "Ground"))
## length of string
print(len(long_string))
## strip white space by default
print(long_string.strip())
## strip whatever you want
str = "000000this is string example...wow!!!00000";
str = str.strip("0")
print(str)
## split a string into a list
list2 = long_string.split(" ")
print(list)
list2 = long_string.split("you")
print(list)

print('\n' * 5)
# lists
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item', grocery_list[0])

grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])
print(grocery_list[1:3])
print('All Items', grocery_list)

other_events = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_events, grocery_list]
to_do_list2 = grocery_list + other_events
print(to_do_list2)

print("All events (separately) =", to_do_list)
print("All events (combined) =", to_do_list2)
print(to_do_list[1][1])

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, 'Pickle')
print(to_do_list)
grocery_list.remove('Pickle')
print(to_do_list)
grocery_list.sort()
print(to_do_list)
grocery_list.reverse()
print(to_do_list)
del grocery_list[1]
print(to_do_list)

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

# tuples
# you cannot change values of a tuple

pi_tuple = (3, 1, 4, 5, 9)
# tuple list conversion
new_list = list(pi_tuple)
new_tuple = tuple(new_list)

print(len(new_tuple), min(new_tuple), max(new_tuple))

# dictionaries or maps
# you cannot join dictionaries together unlike list with +
super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captaion Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pied Piper': 'Thomas Peterson'}

print(super_villains['Captaion Cold'])
del super_villains['Fiddler']
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get('Weather Wizard'))
print(super_villains.keys())
print(super_villains.values())

# conditionals
age = 31
if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')
####
if age >= 21:
    print('You are old enough to drive a tractor trailer')
    print("Good for you!")
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive')
####
if age >= 1 and age <= 18:
    print("You are very young")
elif age > 18 and age < 30:
    print("You are a little bit old")
elif not age == 30:
    print("You are good to go")
else:
    print("Whatever")

# looping for
for x in range(0, 10):
    print(x, ' ', end='')

print("\n")

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

for y in grocery_list:
    print(y, ' ', end='')

print("\n")

for x in [2, 4, 6, 8, 10]:
    print(x, ' ', end='')

print("\n")

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y], ' ', end='')
    print('')

print("\n")

## random number generator
random_num = random.randrange(0, 100)
print("Random num =", random_num)

# looping while
i = 0;

while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 9):
        break  ## ends the while loop
    else:
        i += 1
        continue  ## skips the rest of the while loop
    i += 1


# functions

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


result = addNumber(4, 1)
print("The result is =", result)

## file I/O
'''
file modes
r - Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.
rb - Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
r+ - Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
rb+ - Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.
w - Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
wb - Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
w+ - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
wb+ - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
a - Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
ab - Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
a+ - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
ab+ - Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
'''
## wb - write, ab+ read and append to file (it also opens or creates the file
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

## read information r+ - reading and writing
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()


## delete file
##os.remove("test.txt")

## classes
class Animal:
    ## __ means they are private, for changing or getting them we have to use a function inside of the class
    __name = ""  ## or None
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):  # constructor, it is always like __init__
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):  ## self refers to the object itself, like this in other languages
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):  ## self refers to the object itself, like this in other languages
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):  ## self refers to the object itself, like this in other languages
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):  ## self refers to the object itself, like this in other languages
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}".format(self.__name,
                                                                    self.__height,
                                                                    self.__weight,
                                                                    self.__sound)


## object creation
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())


## inheritance
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(self.get_name(),
                                                                      self.get_height(),
                                                                      self.get_weight(),
                                                                      self.get_sound(),
                                                                      self.__owner)

    def multiple_sounds(self, how_many = None): # how_many = None means it is okey to send nothing for this parameter
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Berkay")
print(spot.toString())

# None parameter (multiple_sounds)
spot.multiple_sounds(4)
spot.multiple_sounds()
## polymorphism
class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)  ## prints animal
test_animals.get_type(spot) ## prints dog

## Input from user

print("What is your name?")
name = sys.stdin.readline()

print("Hello", name)


## libraries
import math ## how to import a library
#help(math) ##  how to get information about the library and its functions


gcdOf = math.gcd(10,15) ## how to use a function in a library
print("The gcd of 10 and 15 =", gcdOf)
print("The gcd of 10 and 15 = {}".format(gcdOf))