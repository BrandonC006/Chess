
#pn = piece names
pn = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
#ps = piece symbols
ps = [['♟', '♞', '♝', '♜', '♛', '♚'], ['♙', '♘', '♗', '♖', '♕', '♔'], [' ']]
#pc = piece color
pc = ['b', 'w']
class Piece:
    def __init__(self, name, symbol, x, y, turns, alive):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.turns = turns
        self.alive = alive
        
    def change_position(self, x, y):
        self.x = x
        self.y = y
    
    def change_turns(self):
        self.turns = self.turns + 1
        
    def change_alive(self):
        self.alive = not self.alive

# black: rook - 0 and 7, knight - 1 and 6, bishop - 2 and 5, queen - 3, king - 4, pawn - 8 to 15
# white: rook - 24 and 31, knight - 25 and 30, bishop - 26 and 29, queen - 27, king - 28, pawn - 16 to 23
pieces: list[Piece] = [Piece(pn[3], ps[1][3], 0, 0, 0, True), Piece(pn[1], ps[1][1], 0, 1, 0, True), Piece(pn[2], ps[1][2], 0, 2, 0, True), Piece(pn[4], ps[1][4], 0, 3, 0, True), Piece(pn[5], ps[1][5], 0, 4, 0, True), Piece(pn[2], ps[1][2], 0, 5, 0, True), Piece(pn[1], ps[1][1], 0, 6, 0, True), Piece(pn[3], ps[1][3], 0, 7, 0, True),
    Piece(pn[0], ps[1][0], 1, 0, 0, True), Piece(pn[0], ps[1][0], 1, 1, 0, True), Piece(pn[0], ps[1][0], 1, 2, 0, True), Piece(pn[0], ps[1][0], 1, 3, 0, True), Piece(pn[0], ps[1][0], 1, 4, 0, True), Piece(pn[0], ps[1][0], 1, 5, 0, True), Piece(pn[0], ps[1][0], 1, 6, 0, True), Piece(pn[0], ps[1][0], 1, 7, 0, True),
    Piece(pn[0], ps[0][0], 6, 0, 0, True), Piece(pn[0], ps[0][0], 6, 1, 0, True), Piece(pn[0], ps[0][0], 6, 2, 0, True), Piece(pn[0], ps[0][0], 6, 3, 0, True), Piece(pn[0], ps[0][0], 6, 4, 0, True), Piece(pn[0], ps[0][0], 6, 5, 0, True), Piece(pn[0], ps[0][0], 6, 6, 0, True), Piece(pn[0], ps[0][0], 6, 7, 0, True),
    Piece(pn[3], ps[0][3], 7, 0, 0, True), Piece(pn[1], ps[0][1], 7, 1, 0, True), Piece(pn[2], ps[0][2], 7, 2, 0, True), Piece(pn[4], ps[0][4], 7, 3, 0, True), Piece(pn[5], ps[0][5], 7, 4, 0, True), Piece(pn[2], ps[0][2], 7, 5, 0, True), Piece(pn[1], ps[0][1], 7, 6, 0, True), Piece(pn[3], ps[0][3], 7, 7, 0, True)]

b_pawn = []
b_knight = []
b_bishop = []
b_rook = []
b_queen = []
b_king = []
w_pawn = []
w_knight = []
w_bishop = []
w_rook = []
w_queen = []
w_king = []

spot_taken = False
for i in range(8):
    print(' ' + ('---' + ' ') * 8, end='\n')
    print('|', end='')
    for j in range(8):
        for k in range(32):
            if pieces[k].x == i and pieces[k].y == j:
                print(' ' + pieces[k].symbol + ' ', end='')
                spot_taken = True
        if not spot_taken:
            print('   ', end='')
        print('|', end='')
        spot_taken = False
    print()
print(' ' + ('---' + ' ') * 8, end='\n')

board = [[ps[0][3], ps[0][1], ps[0][2], ps[0][4], ps[0][5], ps[0][2], ps[0][1], ps[0][3]], 
                      [ps[0][0], ps[0][0], ps[0][0], ps[0][0], ps[0][0], ps[0][0], ps[0][0], ps[0][0]],
                      [ps[2][0] for positions in range(8)], [ps[2][0] for positions in range(8)], [ps[2][0] for positions in range(8)], [ps[2][0] for positions in range(8)],
                      [ps[1][0], ps[1][0], ps[1][0], ps[1][0], ps[1][0], ps[1][0], ps[1][0], ps[1][0]], 
                      [ps[1][3], ps[1][1], ps[1][2], ps[1][4], ps[1][5], ps[1][2], ps[1][1], ps[1][3]]]

def play_game():
    while check_for_checkmate() == False:
        print()
        #TODO

def is_valid_piece(i, j):
    print()

def move_pawn(i1, j1, i2, j2, pawn, opp_piece, real_move):
    # GOES IN MAIN CODE: pawn = check_for_piece(i1, j1) and opp_piece = check_for_piece(i2, j2)
    if pieces[pawn].turns == 0:
        if 8 <= pawn <= 15:
            if (i2 == i1 and j2 == j1 - 2 and pieces[pawn].turns == 0) or (i2 == i1 and j2 == j1 - 1):
                if (real_move):
                    pieces[pawn].change_position(i2, j2)
                    pieces[pawn].change_turns()
                return True
            elif (i2 == i1 + 1 or i2 == i1 - 1) and (j2 == j1 - 1):
                if 16 <= opp_piece <= 31:
                    if (real_move):
                        pieces[pawn].change_position(i2, j2)
                        pieces[pawn].change_turns()
                        pieces[opp_piece].alive = False
                    return True
                elif 0 <= opp_piece <= 15:
                    print('Invalid move')
                    return False
        elif 16 <= pawn <= 23:
            if (i2 == i1 and j2 == j1 + 2 and pieces[pawn].turns == 0) or (i2 == i1 and j2 == j1 + 1):
                if (real_move):
                    pieces[pawn].change_position(i2, j2)
                    pieces[pawn].change_turns()
                return True
            elif (i2 == i1 + 1 or i2 == i1 - 1) and (j2 == j1 + 1):
                if 0 <= opp_piece <= 15:
                    if (real_move):
                        pieces[pawn].change_position(i2, j2)
                        pieces[pawn].change_turns()
                        pieces[opp_piece].alive = False
                    return True
                elif 16 <= opp_piece <= 31:
                    print('Invalid move')
                    return False
        else:
            print('Invalid move')
            return False
        
def move_knight(i1, j1, i2, j2, knight, opp_piece, real_move):
    if (i2 == i1 + 2 and j2 == j1 + 1) or (i2 == i1 + 2 and j2 == j1 - 1) or (i2 == i1 - 2 and j2 == j1 + 1) or (i2 == i1 - 2 and j2 == j1 - 1) or (i2 == i1 + 1 and j2 == j1 + 2) or (i2 == i1 + 1 and j2 == j1 - 2) or (i2 == i1 - 1 and j2 == j1 + 2) or (i2 == i1 - 1 and j2 == j1 - 2):
        if knight == 1 or knight == 6:
            if 16 <= opp_piece <= 32:
                if (real_move):
                    pieces[knight].change_position(i2, j2)
                    pieces[knight].change_turns()
                    pieces[opp_piece].alive = False
                return True
            elif 0 <= opp_piece <= 15:
                print('Invalid move')
                return False
        elif knight == 25 or knight == 30:
            if 0 <= opp_piece <= 15:
                if (real_move):
                    pieces[knight].change_position(i2, j2)
                    pieces[knight].change_turns()
                    pieces[opp_piece].alive = False
                return True
            elif 16 <= opp_piece <= 32:
                print('Invalid move')
                return False
        elif (0 <= i2 <= 7) and (0 <= j2 <= 7):
            if (real_move):
                pieces[knight].change_position(i2, j2)
                pieces[knight].change_turns()
            return True
        else:
            print('Invalid move')
            return False
    
def move_bishop(i1, j1, i2, j2, bishop, opp_piece, real_move):
    if ((i2 - i1) == (j2 - j1)) or ((i2 - i1) == (j2 + j1)):
        pieces[bishop].change_position(i2, j2)
        pieces[bishop].change_turns()
        if (bishop == 2 or bishop == 5) and (16 <= opp_piece <= 32):
            pieces[opp_piece].alive = False
        elif (bishop == 26 or bishop == 29) and (0 <= opp_piece <= 15):
            pieces[opp_piece].alive = False
        return True
    else:
        print('Invalid move')
        return False
    
def move_rook(i1, j1, i2, j2, rook, opp_piece):
    if (i2 == i1) or (j2 == j1):
        pieces[rook].change_position(i2, j2)
        pieces[rook].change_turns()
        if (rook == 3 or rook == 4) and (16 <= opp_piece <= 32):
            pieces[opp_piece].alive = False
        elif (rook == 27 or rook == 28) and (0 <= opp_piece <= 15):
            pieces[opp_piece].alive = False
        return True
    else:
        print('Invalid move')
        return False
    
def move_queen(i1, j1, i2, j2, queen, opp_piece):
    print()
        
def check_for_piece(i, j):
    for k in range(32):
        if pieces[k].x == i and pieces[k].y == j:
            return k
    return 32

def check_for_checkmate(i, j, king):
    if king == 28:
        lower_bound = 0
        upper_bound = 15
    elif king == 4:
        lower_bound = 16
        upper_bound = 31
        
    for k in range(lower_bound, upper_bound):
        for l in range(-1, 1):
            for m in range(-1, 1):
                while pieces[king].x + l >= 0 and pieces[king].x + l <= 7 and pieces[king].y + m >= 0 and pieces[king].y + m <= 7:
                    return True

def send_move(i1, j1, i2, j2, piece, opp_piece, real_move):
    if piece == 0 or piece == 7 or piece == 24 or piece == 31:
        return move_rook(i1, j1, i2, j2, piece, opp_piece)
    elif piece == 1 or piece == 6 or piece == 25 or piece == 30:
        return move_knight(i1, j1, i2, j2, piece, opp_piece, real_move)
    elif piece == 2 or piece == 5 or piece == 26 or piece == 29:
        return move_bishop(i1, j1, i2, j2, piece, opp_piece, real_move)
    elif piece == 3 or piece == 4 or piece == 27 or piece == 28:
        return move_queen(i1, j1, i2, j2, piece, opp_piece)
    elif 8 <= piece <= 15 or 16 <= piece <= 23:
        return move_pawn(i1, j1, i2, j2, piece, opp_piece, False)
    

def check_for_check(i, j, piece):
    if piece == 4:
        for k in range(16, 31):
            send_move(i, j, pieces[k].x, pieces[k].y, k, 32, False)