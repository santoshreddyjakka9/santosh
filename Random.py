import random

letters = "abcdefghijklmno"
print(random.choice(letters))
fruits = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]
print(random.choice(fruits))
salad = random.sample(fruits, 3)
print(salad)