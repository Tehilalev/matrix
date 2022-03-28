import random


my_id = [3, 2, 2, 2, 5, 7, 2, 1, 3]
questions = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
while True:
    _num1 = random.choice(my_id)
    _num2 = random.choice(my_id)
    choice = _num1 + _num2
    if choice < len(questions):
        break

print("The chosen question is: ", questions[choice])
