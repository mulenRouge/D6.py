from random import randint

Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    
    row=input('Пожалуйста, введите строку корабля 1-8 ').upper()
    while row not in '12345678':
        print("Пожалуйста, введите правильную строку")
        row=input('Пожалуйста, введите строку корабля 1-8 ')
    
    column=input('Пожалуйста, введите столбец корабля A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Пожалуйста, введите правильный столбец ")
        column=input('Пожалуйста, введите столбец корабля A-H ')
    return int(row)-1,let_to_num[column]


def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'



def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

create_ships(Hidden_Pattern)

turns = 10
while turns > 0:
    print('Добро пожаловать')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' Начало Боя ')
    elif Hidden_Pattern[row][column] =='X':
        print(' Вы попали!!! ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Вы промазали!')
        Guess_Pattern[row][column] = '-'
        turns -= 1
    if  count_hit_ships(Guess_Pattern) == 5:
        print("Вы потопили Корабль! ")
        break
    print(' Осталось ' +str(turns) + ' ходов ')
    if turns == 0:
        print('Конец игры! ')
        break