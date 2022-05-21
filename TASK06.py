#Реализовать игру камень-ножниц-бумага. Чтобы выйти из игры, чтобы игра не заканчивалась сама по себе, 
# чтобы проверялись введенные данные и не пропускалась какая-либо белиберда

from random import randint

isGame = True
answer = ["камень", "ножницы", "бумага"]

while(isGame):
    player = int(input("Игрок, введите ваш ответ (камень - 1, ножницы - 2, бумага - 3)"))
    computer = randint(1, 3)
    print(f'Игрок - {answer[player - 1]} --- Компьютер {answer[computer - 1]}')

    if player == computer:
        print("Нет победителя")
    
    elif (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("Игрок победил")
    else:
        print("Компьютер победил")

print()
isGame = int(input("Хотите продолжить? (0 - нет, 1 - да)"))