#

# Если в поле цифра, то поле свободно для хода, если X или O - ход сделан
board = list(map(str, range(1, 10)))


# Печать игрового поля
def print_board():
    print(board[:3])
    print(board[3:6])
    print(board[6:])


# Вводим номер поля и проверяем, был ли сделан туда ход
def test_input(XO):  # XO может принимать значения X или O
    field = ' '
    while not field[0].isdigit():
        field = input('Введите номер поля для ' + XO + ' (от 1 до 9): ')
        fieldnum = int(field[0])
        if fieldnum < 1:
            field = ' '
        if board[fieldnum - 1].isdigit():
            board[fieldnum - 1] = XO
        else:
            print('Поле занято')
            field = ' '


if __name__ == '__main__':
    print_board()
    for XO in iter(['X', 'O'] * 2 + ['X']):
        test_input(XO)
        print_board()

