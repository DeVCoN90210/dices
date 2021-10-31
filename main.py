# Импорт модуля Random.
import random
from tkinter import *


def again():
    dices = 0
    roll_again = print()
    while dices == 0:
        # Выбор количества кубиков.
        chosen_dices = int(input("How many dices do you want to roll? (from 1 to 5): "))
        if chosen_dices > 0 and chosen_dices < 6:
            break

    # Выкидывает кубики после выбора количества. Т.к все кубики размера D6, генерируется число от 1 до 6.
    if chosen_dices == 1:
        while dices < 1:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 2:
        while dices < 2:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 3:
        while dices < 3:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 4:
        while dices < 4:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    elif chosen_dices == 5:
        while dices < 5:
            rolls = random.randint(1, 6)
            print(rolls)
            dices += 1

    # Спрашивает пользователя надо ли повторить бросок.
    print("Do you want to roll again?")
    while roll_again != "Yes" or roll_again != "No":
        roll_again = input("Yes - Y | No - N: ").lower().capitalize()
        # Если да - начать всё заново.
        if roll_again == "Y":
            again()
            break
        # Если нет, прервать исполнение.
        if roll_again == "N":
            print("Goodbye")
            break
# Закрытие функции.
again()