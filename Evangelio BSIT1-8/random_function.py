import random

fruits = ["apple", "banana", "grapes", "avocado"]

random_num = random.randint(1,10)
print("Random Number Generated:", random_num)

random_fruit = random.choice(fruits)
print("Random Fruit Picked:", random_fruit)