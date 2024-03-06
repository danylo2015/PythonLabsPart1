"""
Importing the Enum from enum module and also dataclass
"""

from enum import Enum
from dataclasses import dataclass


class Kind(Enum):
    """
    This is class Kind
    """

    DOG = 1
    CAT = 2
    BIRD = 3


@dataclass(eq=False)
class Pet:
    """
    This is class Pet with is_polite method
    """
    name: str
    breed: str
    age: int
    greeting: str
    mass: float
    kind: Kind

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

    def add_pet(self, new_pet):
        """
        Add a pet to the home if a pet with the same parameters doesn't exist.
        """
        if new_pet not in self.pets:
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
