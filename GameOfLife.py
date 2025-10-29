#defines "board_setup"

#globals
squares = [] #all the squares            :str
pieces = [] #all the pieces locations    :str



def board_setup():
    letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        for number in range(8):
            squares.append(letter[i]+str(number+1))

#current_square format = letter+number   :str


def rook(current_square, pieces): 
    available_moves = []
    #check up direction
    def up():
        plus = 0
        plus += 1
        column = int(current_square[1]) + plus
        while column < 8:
            if current_square[0] + str(int(current_square[1]) + plus) not in pieces:
                available_moves.append(current_square[0] + str(int(current_square[1]) + plus))
                column = int(current_square[1]) + plus
                print(f"No piece is on {current_square[0] + str(int(current_square[1]) + plus)}")
            else:
                print(f"A piece is obstructing on the square {current_square[0] + str(int(current_square[1]) + plus)}")
                break
            plus += 1

    #check down direction
    def down():
        plus = 0
        plus -= 1
        column = int(current_square[1]) + plus
        while column > 0:
            if current_square[0] + str(int(current_square[1]) + plus) not in pieces:
                available_moves.append(current_square[0] + str(int(current_square[1]) + plus))
                column = int(current_square[1]) + plus
                print(f"No piece is on {current_square[0] + str(int(current_square[1]) + plus)}")
            else:
                print(f"A piece is obstructing on the square {current_square[0] + str(int(current_square[1]) + plus)}")
                break
            plus -= 1

    #check right direction
    def right():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus = 0
        plus += 1
        row = letters[letters_index + plus]
        while row != "h" and (letters_index+plus) >= 0:
            if letters[letters_index + plus] + current_square[1] not in pieces:
                available_moves.append(letters[letters_index + plus] + current_square[1])
                row = letters[letters_index + plus]
                print(f"No piece is on {letters[letters_index + plus] + current_square[1]}")
            else:
                print(f"A piece is obstructing on the square {letters[letters_index + plus] + current_square[1]}")
                break
            plus += 1

    #check left direction
    def left():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus = 0
        plus -= 1
        row = letters[letters_index + plus]
        while row != "a" and (letters_index+plus) >= 0:
            if letters[letters_index + plus] + current_square[1] not in pieces:
                available_moves.append(letters[letters_index + plus] + current_square[1])
                row = letters[letters_index + plus]
                print(f"No piece is on {letters[letters_index + plus] + current_square[1]}")
            else:
                print(f"A piece is obstructing on the square {letters[letters_index + plus] + current_square[1]}")
                break
            plus -= 1


    up()
    down()
    left()
    right()
    sorted(available_moves)
    return available_moves

def bishop(current_square, pieces):
    available_moves = []

    #check left up diagonal
    def left_up():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus_row = 0
        plus_column = 0
        plus_row -= 1
        plus_column += 1
        column = int(current_square[1]) + plus_column
        if letters_index + plus_row > 0:
            row = letters[letters_index + plus_row]
            while column <= 8 and row != "a":
                if letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column) not in pieces:
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
                    column = int(current_square[1]) + plus_column
                    row = letters[letters_index + plus_row]
                else:
                    print(f"A piece is obstructing on {letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column)}")
                    break
                plus_row -= 1
                plus_column += 1

    #check left down diagonal
    def left_down():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus_row = 0
        plus_column = 0
        plus_row -= 1
        plus_column -= 1
        column = int(current_square[1]) + plus_column
        if letters_index + plus_row > 0:
            row = letters[letters_index + plus_row]
            while column > 0 and row != "a":
                if letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column) not in pieces:
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
                    column = int(current_square[1]) + plus_column
                    row = letters[letters_index + plus_row]
                else:
                    print(f"A piece is obstructing on {letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column)}")
                    break
                plus_row -= 1
                plus_column -= 1

    #check right up diagonal
    def right_up():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus_row = 0
        plus_column = 0
        plus_row += 1
        plus_column += 1
        column = int(current_square[1]) + plus_column
        if letters_index + plus_row < 8:
            row = letters[letters_index + plus_row]
            while column <= 8 and row != "h":
                if letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column) not in pieces:
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
                    column = int(current_square[1]) + plus_column
                    row = letters[letters_index + plus_row]
                else:
                    print(f"A piece is obstructing on {letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column)}")
                    break
                plus_row += 1
                plus_column += 1

    #check right down diagonal
    def right_down():
        letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for i in range(8):
            if current_square[0] == letters[i]:
                letters_index = i
        plus_row = 0
        plus_column = 0
        plus_row += 1
        plus_column -= 1
        column = int(current_square[1]) + plus_column
        if letters_index + plus_row < 8:
            row = letters[letters_index + plus_row]
            while column > 0 and row != "h":
                if letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column) not in pieces:
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
                    column = int(current_square[1]) + plus_column
                    row = letters[letters_index + plus_row]
                else:
                    print(f"A piece is obstructing on {letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column)}")
                    break
                plus_row += 1
                plus_column -= 1

    left_up()
    left_down()
    right_up()
    right_down()
    sorted(available_moves)
    return available_moves

def queen(current_square, pieces):
    available_moves = []
    available_moves_rook = rook(current_square, pieces)
    available_moves_bishop = bishop(current_square, pieces)
    for i in range(len(available_moves_rook)):
        available_moves.append(available_moves_rook[i])
    for i in range(len(available_moves_bishop)):
        available_moves.append(available_moves_bishop[i])
    
    return available_moves

def knight(current_square, pieces):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i

    def up():
        if int(current_square[1]) + 2 <= 8:
            if current_square[0] == "a":
                if letters[letters_index + 1] + str(int(current_square[1]) + 2) not in pieces:
                    available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 2))
            elif current_square[0] == "h":
                if letters[letters_index - 1] + str(int(current_square[1]) + 2) not in pieces:
                    available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 2))
            else:
                if letters[letters_index - 1] + str(int(current_square[1]) + 2) not in pieces:
                    available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 2))
                if letters[letters_index + 1] + str(int(current_square[1]) + 2) not in pieces:
                    available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 2))

    def down():
        if int(current_square[1]) - 2 >= 0:
            if current_square[0] == "a":
                if letters[letters_index + 1] + str(int(current_square[1]) - 2) not in pieces:
                    available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 2))
            elif current_square[0] == "h":
                if letters[letters_index - 1] + str(int(current_square[1]) - 2) not in pieces:
                    available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 2))
            else:
                if letters[letters_index - 1] + str(int(current_square[1]) - 2) not in pieces:
                    available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 2))
                if letters[letters_index + 1] + str(int(current_square[1]) - 2) not in pieces:
                    available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 2))
    
    def left():
        if letters_index - 2 >= 0:
            if int(current_square[1]) == 1:
                if letters[letters_index - 2] + str(int(current_square[1]) + 1) not in pieces:
                    available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) + 1))
            elif int(current_square[1]) == 8:
                if letters[letters_index - 2] + str(int(current_square[1]) - 1) not in pieces:
                    available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) - 1))
            else:
                if letters[letters_index - 2] + str(int(current_square[1]) + 1) not in pieces:
                    available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) + 1))
                if letters[letters_index - 2] + str(int(current_square[1]) - 1) not in pieces:
                    available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) - 1))

    def right():
        if letters_index + 2 <= 8:
            if int(current_square[1]) == 1:
                if letters[letters_index + 2] + str(int(current_square[1]) + 1) not in pieces:
                    available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) + 1))
            elif int(current_square[1]) == 8:
                if letters[letters_index + 2] + str(int(current_square[1]) - 1) not in pieces:
                    available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) - 1))
            else:
                if letters[letters_index + 2] + str(int(current_square[1]) + 1) not in pieces:
                    available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) + 1))
                if letters[letters_index + 2] + str(int(current_square[1]) - 1) not in pieces:
                    available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) - 1))

    up()
    down()
    left()
    right()
    return sorted(available_moves)





#testing

board_setup()
print(knight("e5", ["b2"]))








#mango
