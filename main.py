import random
import time
player = ['Красный','Синий','Зеленый','Розовый','Оранжевый',
          'Желтый','Черный','Белый','Фиолетовый','Коричневый','Бирюзовый']
print("Добро пожаловатьв Impostor!\nЦель - Найти придателя из игроков!\nЖелаем удачи!")
time.sleep(5)
x = 12
while x != 0:
    print("Список игроков:")
    for q in player: print(q)
    pla = input("Кого вы подозреваете?\n")
    k = player.remove(pla)
    if x == random.randint(0,x):
        x = 0
        print('.....Голосование.....')
        time.sleep(3)
        print(pla + ' был предателем!\nНадеемся что мы его больше не увидим!\nСпасибо тебе!')
    else:
        print('.....Голосование.....')
        time.sleep(3)
        print(pla + ' небыл предателем!\n\n')
        time.sleep(3)
        x=x-1
