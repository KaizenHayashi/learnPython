import random

def roll_dice(num):
    return random.randint(1, num)

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honour_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

class Chef:
    def make_chicken(self):
        print("The chef makes a chicken.\n")

    def make_salad(self):
        print("The chef makes a salad.\n")

    def make_pasta(self):
        print("The chef makes pasta.\n")