from pets import Pet, Home, Kind

dog = Pet("Buddy", "Golden Retriever", 3, "Hello, I'm Buddy!", 30, Kind.DOG)
cat = Pet("Kitty", "Siamese", 2, "Meow!", 10, Kind.CAT)
bird = Pet("Polly", "Parrot", 1, "Hello, I'm Polly!", 1, Kind.BIRD)

home = Home()
home.add_pet(dog)
home.add_pet(cat)
home.add_pet(bird)

print(home.friends_of_pet(dog))
print(home.friends_of_pet(cat))
print(home.friends_of_pet(bird))
for pet in home.pets:
    print(f"{pet.name} is polite: {pet.is_polite()}")


home.sort_pets_by_age()
print("Pets sorted by age:")
for pet in home.pets:
    print(f"{pet.name} - {pet.age} years old")
