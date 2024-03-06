import math
import requests

url = "https://www.example.com"
response = requests.get(url)
print(response.text)


animal = "cat"
print(animal)

is_weekend = True
is_mammal = True
has_wings = True
print(is_weekend and is_mammal and has_wings)

x = 1.839
y = 3.821
z = 0.349
a = x ** (y + z) + math.sqrt(x + (z ** y)) - 161 * math.tan(x * z)
print(a)
