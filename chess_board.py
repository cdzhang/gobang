
class chessBoard:
    WHITE = -1
    BLACK = 1
    EMPTY = 0
    FULL = 2
    def __init__(self,row_count=15,col_count=15):
        self.board = [[0 for i in range(col_count)] for j in range(row_count)]
        self.row_count = row_count
        self.col_count = col_count

    def move(self,i,j,who):
        '''
        put chess piece at location i,j
        return:: True is sucess, else False
        '''
        if self.board[i][j] != chessBoard.EMPTY:
            return False
        if who not in [chessBoard.BLACK,chessBoard.WHITE]:
            return False
        self.board[i][j] = who
        return True

    def get_status_after_move(self,i,j):
        '''
        check whether player wins after moving in position i,j
        return:
        chessBoard.WHITE, if white wins
        chessBoard.BLACK, if black wins
        0: nobody wins
        '''
        who = self.board[i][j]
        if who == chessBoard.EMPTY:
            return 0
        pair_directions = [(0,1),(1,0),(1,1),(1,-1)]

        for direction in pair_directions:
            if self.count_direction(i,j,direction,who)>=5:
                return who
        return 0

    def count_direction(self,i,j,direction,who):
        '''
        count the maximum counters in a row along direction
        return: int
        '''
        x,y = i,j
        di,dj = direction
        count = 0
        while (x>=0 and x<self.row_count) and (y>=0 and y<self.col_count):
            x = x+di
            y = y+dj
            if self.board[x][y] == who:
                count += 1
            else:
                break

        x,y = i,j
        while (x>=0 and x<self.row_count) and (y>=0 and y<self.col_count):
            x = x-di
            y = y-dj
            if self.board[x][y] == who:
                count += 1
            else:
                break
        return count + 1


    def print_board(self):
        '''
        print chess board
        '''
        dic = {1:'* ',-1:'# ',0:'. '}
        for row in self.board:
            print("".join([dic[e] for e in row]))

class AI:
    def __init__(self,chess_board=None):
        if not chess_board:
            chess_board = chessBoard()
        self.board = chess_board
        

class god:
    def play(self,player1,player2,wait1=0,wait2=0,print_details=False):
        '''
        simuate play of player1 and player2
        player is an instance that contains the method get_move(board)
        wait: wait after every move?
        result:
        '''


if __name__ == '__main__':
    chess_board = chessBoard()
    for i in range(5):
        chess_board.move(i+3,-i+7,-1)
    chess_board.print_board()
    for i in range(8):
        print(chess_board.get_status_after_move(i+3,i+7))
