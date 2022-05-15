# Крестики - нолики
import os
os.system('cls')


def draw_desk(desk):
    print('-'*13)
    for i in range(3):
        print('|', desk[0 + i*3], '|', desk[1 + i*3], '|', desk[2 + i*3], '|')
        print('-'*13)
        
def take_choice(player_choice):
    flag = False
    while not flag:
        player_answer = input('В какую клеточку ставим ' + player_choice + '? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Ошибка ввода. Введите число клеточки')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(desk[player_answer - 1]) not in 'XO'):
                desk[player_answer - 1] = player_choice
                flag = True
            else:
                print('Указанная клетка уже занята')
        else:
            print('Введите число клеточки от 1 до 9')
    return desk

def check_win(desk):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if desk[i[0]] == desk[i[1]] == desk[i[2]]:
            return desk[i[0]]
    return False

def main(desk):
    counter = 0
    win = False
    while not win:
        draw_desk(desk)
        if counter % 2 == 0:
            take_choice('X')
        else:
            take_choice('O')
        counter += 1
        if counter > 4:
            tmp = check_win(desk)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print('У нас - Ничья!')
            break
    draw_desk(desk)

print('Начинаем нашу игру')
desk = list(range(1, 10))
main(desk)