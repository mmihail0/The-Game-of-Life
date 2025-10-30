#defines "board_setup"

#globals
squares = [] #all the squares                                                          :str
pieces = [] #all the pieces locations                                                  :str
pieces_white = [] #all of whites pieces locations                                      :str
pieces_black = [] #all of blacks pieces locations                                      :str
covered_squares_white = [] #all squares that white coveres - black king cant go there  :str
covered_squares_black = [] #all squares that black coveres - white king cant go there  :str
#current_square format = letter+number                                                 :str



def board_setup():
    letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        for number in range(8):
            squares.append(letter[i]+str(number+1))



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
                print(f"A piece is obstructing on the square {current_square[0] + str(int(current_square[1]) + plus)} so you can take it")
                available_moves.append(current_square[0] + str(int(current_square[1]) + plus))
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
                available_moves.append(current_square[0] + str(int(current_square[1]) + plus))
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
                available_moves.append(letters[letters_index + plus] + current_square[1])
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
                available_moves.append(letters[letters_index + plus] + current_square[1])
                break
            plus -= 1


    up()
    down()
    left()
    right()
    return sorted(available_moves)

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
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
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
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
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
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
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
                    available_moves.append(letters[letters_index + plus_row] + str(int(current_square[1]) + plus_column))
                    break
                plus_row += 1
                plus_column -= 1

    left_up()
    left_down()
    right_up()
    right_down()
    return sorted(available_moves)

def queen(current_square, pieces):
    available_moves = []
    available_moves_rook = rook(current_square, pieces)
    available_moves_bishop = bishop(current_square, pieces)
    for i in range(len(available_moves_rook)):
        available_moves.append(available_moves_rook[i])
    for i in range(len(available_moves_bishop)):
        available_moves.append(available_moves_bishop[i])
    
    return available_moves

def knight(current_square):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i

    def up():
        if int(current_square[1]) + 2 <= 8:
            if current_square[0] == "a":
                available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 2))
            elif current_square[0] == "h":
                available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 2))
            else:
                available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 2))
                available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 2))

    def down():
        if int(current_square[1]) - 2 >= 0:
            if current_square[0] == "a":
                available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 2))
            elif current_square[0] == "h":
                available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 2))
            else:
                available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 2))
                available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 2))
    
    def left():
        if letters_index - 2 >= 0:
            if int(current_square[1]) == 1:
                available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) + 1))
            elif int(current_square[1]) == 8:
                available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) - 1))
            else:
                available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) + 1))
                available_moves.append(letters[letters_index - 2] + str(int(current_square[1]) - 1))

    def right():
        if letters_index + 2 <= 8:
            if int(current_square[1]) == 1:
                available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) + 1))
            elif int(current_square[1]) == 8:
                available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) - 1))
            else:
                available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) + 1))
                available_moves.append(letters[letters_index + 2] + str(int(current_square[1]) - 1))

    up()
    down()
    left()
    right()
    return sorted(available_moves)

def pawn_white(current_square, pieces, previous_move, double_move):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i

    #movement
    if current_square[0] + str(int(current_square[1]) + 1) not in pieces: #move 1 square
        available_moves.append(current_square[0] + str(int(current_square[1]) + 1))
        if current_square[0] + str(int(current_square[1]) + 2) not in pieces and int(current_square[1]) == 2: #move 2 squares if still on the 2nd rank
            available_moves.append(current_square[0] + str(int(current_square[1]) + 2))
    #capturing
    if current_square[0] != "h":
        if letters[letters_index + 1] + str(int(current_square[1]) + 1) in pieces: #capturing to the right
            available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 1))
    if current_square[0] != "a":
        if letters[letters_index - 1] + str(int(current_square[1]) + 1) in pieces: #capturing to the left
            available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 1))
    #enpassant
    '''if previous_move[0].islower() :
        if double_move == True:'''

def pawn_black(current_square, pieces, previous_move, double_move):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i

    #movement
    if current_square[0] + str(int(current_square[1]) - 1) not in pieces: #move 1 square
        available_moves.append(current_square[0] + str(int(current_square[1]) - 1))
        if current_square[0] + str(int(current_square[1]) - 2) not in pieces and int(current_square[1]) == 7: #move 2 squares if still on the 2nd rank
            available_moves.append(current_square[0] + str(int(current_square[1]) - 2))
    #capturing
    if current_square[0] != "h":
        if letters[letters_index + 1] + str(int(current_square[1]) - 1) in pieces: #capturing to the right
            available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 1))
    if current_square[0] != "a":
        if letters[letters_index - 1] + str(int(current_square[1]) - 1) in pieces: #capturing to the left
            available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 1))
    #enpassant
    '''if previous_move[0].islower() :
        if double_move == True:'''

def king_white(current_square, pieces, covered_squares_black):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i
    #perpendicular movement
    if current_square[0] + str(int(current_square[1]) + 1) not in pieces and current_square[0] + str(int(current_square[1]) + 1) not in covered_squares_black and int(current_square[1]) != 8: #move up
        available_moves.append(current_square[0] + str(int(current_square[1]) + 1))
    if current_square[0] + str(int(current_square[1]) - 1) not in pieces and current_square[0] + str(int(current_square[1]) - 1) not in covered_squares_black and int(current_square[1]) != 1: #move down
        available_moves.append(current_square[0] + str(int(current_square[1]) - 1))
    if letters[letters_index + 1] + current_square[1] not in pieces and letters[letters_index + 1] + current_square[1] not in covered_squares_black and current_square[0] != "h": #move right
        available_moves.append(letters[letters_index + 1] + current_square[1])
    if letters[letters_index - 1] + current_square[1] not in pieces and letters[letters_index - 1] + current_square[1] not in covered_squares_black and current_square[0] != "a": #move left
        available_moves.append(letters[letters_index - 1] + current_square[1])
    #diagonal movement
    if letters[letters_index + 1] + str(int(current_square[1]) + 1) not in pieces and letters[letters_index + 1] + str(int(current_square[1]) + 1) not in covered_squares_black and int(current_square[1]) != 8 and current_square[0] != "h": #move right-up
        available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 1))
    if letters[letters_index + 1] + str(int(current_square[1]) - 1) not in pieces and letters[letters_index + 1] + str(int(current_square[1]) - 1) not in covered_squares_black and int(current_square[1]) != 1 and current_square[0] != "h": #move right-down
        available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 1))
    if letters[letters_index - 1] + str(int(current_square[1]) + 1) not in pieces and letters[letters_index - 1] + str(int(current_square[1]) + 1) not in covered_squares_black and int(current_square[1]) != 8 and current_square[0] != "a": #move left-up
        available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 1))
    if letters[letters_index - 1] + str(int(current_square[1]) - 1) not in pieces and letters[letters_index - 1] + str(int(current_square[1]) - 1) not in covered_squares_black and int(current_square[1]) != 1 and current_square[0] != "a": #move left-down
        available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 1))

    return sorted(available_moves)

def king_black(current_square, pieces, covered_squares_white):
    available_moves = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(8):
        if current_square[0] == letters[i]:
            letters_index = i
    #perpendicular movement
    if current_square[0] + str(int(current_square[1]) + 1) not in pieces and current_square[0] + str(int(current_square[1]) + 1) not in covered_squares_white and int(current_square[1]) != 8: #move up
        available_moves.append(current_square[0] + str(int(current_square[1]) + 1))
    if current_square[0] + str(int(current_square[1]) - 1) not in pieces and current_square[0] + str(int(current_square[1]) - 1) not in covered_squares_white and int(current_square[1]) != 1: #move down
        available_moves.append(current_square[0] + str(int(current_square[1]) - 1))
    if letters[letters_index + 1] + current_square[1] not in pieces and letters[letters_index + 1] + current_square[1] not in covered_squares_white and current_square[0] != "h": #move right
        available_moves.append(letters[letters_index + 1] + current_square[1])
    if letters[letters_index - 1] + current_square[1] not in pieces and letters[letters_index - 1] + current_square[1] not in covered_squares_white and current_square[0] != "a": #move left
        available_moves.append(letters[letters_index - 1] + current_square[1])
    #diagonal movement
    if letters[letters_index + 1] + str(int(current_square[1]) + 1) not in pieces and letters[letters_index + 1] + str(int(current_square[1]) + 1) not in covered_squares_white and int(current_square[1]) != 8 and current_square[0] != "h": #move right-up
        available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) + 1))
    if letters[letters_index + 1] + str(int(current_square[1]) - 1) not in pieces and letters[letters_index + 1] + str(int(current_square[1]) - 1) not in covered_squares_white and int(current_square[1]) != 1 and current_square[0] != "h": #move right-down
        available_moves.append(letters[letters_index + 1] + str(int(current_square[1]) - 1))
    if letters[letters_index - 1] + str(int(current_square[1]) + 1) not in pieces and letters[letters_index - 1] + str(int(current_square[1]) + 1) not in covered_squares_white and int(current_square[1]) != 8 and current_square[0] != "a": #move left-up
        available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) + 1))
    if letters[letters_index - 1] + str(int(current_square[1]) - 1) not in pieces and letters[letters_index - 1] + str(int(current_square[1]) - 1) not in covered_squares_white and int(current_square[1]) != 1 and current_square[0] != "a": #move left-down
        available_moves.append(letters[letters_index - 1] + str(int(current_square[1]) - 1))

    return sorted(available_moves)




#testing

board_setup()
print(king_white("a1"))








#mango
