import random

number = random.randint(1, 10)
attempts = 3

for i in range(attempts):
    guess = int(input("Введіть число від 1 до 10: "))
    if guess < number:
        print("Більше")
    elif guess > number:
        print("Менше")
    else:
        print("Ви вгадали!")
        break
else:
    print(f"Ви програли! Загадане число було {number}")
