"""
Importing pytest module and classes Pet, Home, Kind from pet.py
"""
import pytest
from pet import Pet, Home, Kind


@pytest.fixture(name="home2")
def home():
    """
    Initialize pets
    """
    home1 = Home()
    dog1 = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)
    dog2 = Pet("Whiskers", "Siamese", 2, "Meow!", 10, Kind.DOG)
    dog3 = Pet("Tweety", "Canary", 7, "Chirp chirp!", 0.5, Kind.DOG)
    home1.add_pet(dog1)
    home1.add_pet(dog2)
    home1.add_pet(dog3)
    return home1


def test_add_pet_negative():
    """tests add_pet in negative conditions"""
    home_test = Home()

    pet = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)
    pet3 = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)
    pet2 = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)

    home_test.add_pet(pet)
    home_test.add_pet(pet3)
    home_test.add_pet(pet2)
    home_test.add_pet(pet)
    home_test.add_pet(pet3)
    home_test.add_pet(pet2)

    assert len(home_test.pets) == 3


def test_add_pet():
    """tests add_pet"""
    home_test = Home()

    pet = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)
    pet2 = Pet("Bluddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)

    home_test.add_pet(pet)
    home_test.add_pet(pet2)
    assert len(home_test.pets) == 2


def test_is_polite():
    """
    This func tests if is_polite works correctly
    """
    pet = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 25, Kind.DOG)
    assert pet.is_polite() is True


def test_is_not_polite():
    """
    This func tests if is_polite works correctly for a not polite pet
    """
    grumpy_cat = Pet("Whiskers", "Persian Cat", 5, "NO!", 10, Kind.CAT)
    assert grumpy_cat.is_polite() is False


def test_are_friends(home2):
    """
    This func tests if are_friends works correctly for a not polite pet
    """
    pet = Pet("Blud", "Golden Retriever", 4, "Hello, I'm Buddy!", 25, Kind.DOG)
    friends = home2.are_friends(pet)
    assert len(friends) == 1


def test_friends_of_pet(home2):
    """
    This func tests if friends_of_pet works correctly
    """
    dog = Pet("Blud", "Golden Retriever", 10, "Hello, I'm Buddy!", 30, Kind.DOG)
    cat = Pet("Kitty", "Siamese", 2, "Meow!", 10, Kind.CAT)

    assert home2.friends_of_pet(dog) == "Blud has no friends"
    assert home2.friends_of_pet(cat) == "Friends of Kitty: Buddy, Whiskers"


def test_sort_pets_by_age(home2):
    """
    This func tests if sort_pets_by_age works correctly
    """
    home2.sort_pets_by_age()
    ages = [pet.age for pet in home2.pets]
    assert ages == sorted(ages)
