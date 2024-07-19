import random

def display(board, his):
    print("4 colors: R, G, B, Y")
    print("P = position correct, with correct color")
    print("C = correct color, but wrong position")
    print("---+---+---+---+------")
    for i in range(0, 32, 4):
        print(f" {board[i]}   {board[i + 1]}   {board[i + 2]}   {board[i + 3]}   {his[i // 4]}")
        print("---+---+---+---+------")

def getinput(board, his, result, q):
    p = 0
    c = 0
    temp = result
    for i in range(0, 32):
        if board[i] == '':
            current_index = i
            break
    move = [''] * 4
    move = input("Enter your guess (using R, G, B, Y): ")
    if all(char in ['R', 'G', 'B', 'Y'] for char in move):
        board[current_index:current_index + 4] = [char for char in move]
        for i in range(0, 4):
            if result[i] == board[i + current_index]:
                p += 1
            if board[i + current_index] in temp:
                c += 1
                for j in range(len(temp)):
                    if temp[j] == board[i + current_index]:
                        temp[j] = ' '
                        break
        c -= p
        his[q] = f"{p}P{c}C"
        if len(his) >= 8:
            return
    else:
        print("Invalid input. Please use only R, G, B, or Y.")


def gen():
    colors = ['R', 'G', 'B', 'Y']
    return [random.choice(colors) for _ in range(4)]

def play():
    print("Welcome to Master Mind!")
    result = gen()
    #print(result)
    board = [''] * 32
    his = [''] * 8
    i = 0
    while i != 8:
        getinput(board, his, result, i)
        display(board, his)
        #print(his[i])
        if his[i] == "4P0C":
            print("You Win!")
            return
        i += 1
    print("You Lose!")
    return

play()