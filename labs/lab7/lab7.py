"""
Importing the Enum from enum module
"""

import logging
from enum import Enum


def logged(exception, mode):
    """
    Parameterized decorator that logs exceptions in the specified mode.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.ERROR)
                    logging.error(e)
        return wrapper
    return decorator


class InvalidAgeError(Exception):
    """
    Custom exception raised when an invalid age is entered for a pet.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Kind(Enum):
    """
    This is class Kind
    """

    DOG = 1
    CAT = 2
    BIRD = 3


class Pet:
    """
    This is class Pet with is_polite method
    """

    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def is_polite(self):
        """Check if the greeting contains 'Hello'."""
        return "Hello" in self.greeting

    def __str__(self):
        return f"{self.name}, {self.age}, {self.mass}, {self.kind}, {self.breed}"


class Home:
    """
    This is class Home with add_pet, are_friends,
    friends_of_pet and sort_pets_by_age methods
    """

    def __init__(self):
        self.pets = []

    @logged(InvalidAgeError, "file")
    def add_pet(self, new_pet):
        """
        Add a pet to the home if a pet with the same parameters doesn't exist.
        """
        if new_pet not in self.pets:
            if new_pet.age < 0:
                raise InvalidAgeError("Invalid age: Age must be non-negative.")
            self.pets.append(new_pet)
        else:
            print(f"{new_pet.name} is already in the home.")

    def are_friends(self, pet2):
        """Find friends of a pet based on age."""
        return [other_pet for other_pet in self.pets if abs(pet2.age - other_pet.age) < 2]

    def friends_of_pet(self, other_pet):
        """Get friends' names of a pet."""
        friends_of_pet = self.are_friends(other_pet)
        if friends_of_pet:
            friends_names = [
                friend.name for friend in friends_of_pet
                if friend.name != other_pet.name
            ]
            if friends_names:
                return f"Friends of {other_pet.name}: {', '.join(friends_names)}"
        return f"{other_pet.name} has no friends"

    def sort_pets_by_age(self):
        """Sort pets by age."""
        self.pets.sort(key=lambda x: x.age)


home = Home()

invalid_age_pet = Pet(name="Fluffy", breed="Persian", age=-1, greeting="Meow", mass=5, kind=Kind.CAT)

home.add_pet(invalid_age_pet)
