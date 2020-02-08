import os
import copy
import sys
# sys.setrecursionlimit(362880)

player = "X"
cpu = "O"


def displayBoard(x):
    os.system('cls')
    print(' {:1} | {:1} | {:1} '.format(x[6], x[7], x[8]))
    print('---+---+---')
    print(' {:1} | {:1} | {:1} '.format(x[3], x[4], x[5]))
    print('---+---+---')
    print(' {:1} | {:1} | {:1} '.format(x[0], x[1], x[2]))


def checkwin(lst):
    if lst[0] == lst[3] == lst[6] == player or lst[0] == lst[4] == lst[8] == player or lst[0] == lst[1] == lst[2] == player or lst[8] == lst[7] == lst[6] == player or lst[8] == lst[5] == lst[2] == player or lst[6] == lst[4] == lst[2] == player or lst[1] == lst[4] == lst[7] == player or lst[3] == lst[4] == lst[5] == player:
        return player
    if lst[0] == lst[3] == lst[6] == cpu or lst[0] == lst[4] == lst[8] == cpu or lst[0] == lst[1] == lst[2] == cpu or lst[8] == lst[7] == lst[6] == cpu or lst[8] == lst[5] == lst[2] == cpu or lst[6] == lst[4] == lst[2] == cpu or lst[1] == lst[4] == lst[7] == cpu or lst[3] == lst[4] == lst[5] == cpu:
        return cpu
    else:
        return 'NO'


def heuristic(temp, pos, turn):
    temp[pos] = turn
    result=checkwin(temp)
    if  result != 'NO':
        if result == cpu:
            temp[pos] = ' '
            return 100
        elif result==player:
            temp[pos] = ' '
            return -100
    if ' ' not in temp:
        temp[pos] = ' '
        return 0
    h = {}
    for i in range(9):
        if temp[i] == ' ':
            if turn == cpu:
                h[i] = heuristic(temp, i, player)
            elif turn == player:
                h[i] = heuristic(temp, i, cpu)
    
    temp[pos] = ' '

    if turn == player:
        hur= h[max(h, key=h.get)]
        return hur
    elif turn == cpu:
        hur = h[min(h ,key=h.get)]
        return hur


def getpostion(lst):
    temp = [i for i in lst]
    h = {}
    for i in range(9):
        if temp[i] == ' ':
            h[i] = heuristic(temp, i, cpu)
    pos = max(h, key=h.get)
    return pos


matrix = []
for _ in range(9):
    matrix.append(' ')
while(1):
    c = checkwin(matrix)
    if c == player:
        print("\n\n\t\t\tPlayer Wins")
        break
    elif c == cpu:
        print("Computer wins")
        break
    if ' ' not in matrix:
        print("\n\n\t\tIts A Draw\n\n")
        break
    while True:
        pos = int(input("Please Enter the Positition You want to enter: ").strip())
        if matrix[pos-1] ==' ':
            matrix[pos-1] = player
            break
        else:
            print("Position Already Filled. Try again later\a\a")
    displayBoard(matrix)
    c = checkwin(matrix)
    if c == player:
        print("\n\n\t\t\tPlayer Wins")
        break
    elif c == cpu:
        print("Computer wins")
        break
    if ' ' not in matrix:
        print("\n\n\t\tIts A Draw\b\b\n\n\b")
        break
    pos = getpostion(matrix)
    matrix[pos] = cpu
    displayBoard(matrix)
input("Please Press Enter To Exit ....")