
import random,time

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
                print(i,j)
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

            if self.board[x][y] == who:
                count += 1
            else:
                break
            x = x+di
            y = y+dj

        x,y = i,j
        while (x>=0 and x<self.row_count) and (y>=0 and y<self.col_count):
            if self.board[x][y] == who:
                count += 1
            else:
                break
            x = x-di
            y = y-dj

        return count - 1


    def print_board(self):
        '''
        print chess board
        '''
        dic = {1:'* ',-1:'# ',0:'. '}
        for row in self.board:
            print("".join([dic[e] for e in row]))
        print()

class Player:
    def __init__(self):
        self.name = self.get_player_name()

    def get_player_name(self):
        raise NotImplementedError

    def next_move(self,chess_board,who):
        '''
        decide the next move
        chess_board: chessBoard
        who: chessBoard.WHITE, chessBoard.BLAKC
        '''
        raise NotImplementedError

class randomPlayer:
    def get_player_name(self):
        return "random player"

    def next_move(self,chess_board,who):
        '''
        randomly choose an aviable slot for the next move
        chess_board: chessBoard
        who: chessBoard.WHITE, chessBoard.BLAKC
        '''
        empty_list = []
        for i in range(chess_board.row_count):
            for j in range(chess_board.col_count):
                if chess_board.board[i][j] == chessBoard.EMPTY:
                    empty_list.append((i,j))
        if len(empty_list) == 0:
            print("game over")
            return None

        return random.sample(empty_list,1)[0]

class godVision:
    def play(self,player1,player2,wait1=0,wait2=0,print_details=False):
        '''
        simuate play of player1 and player2
        player is an instance that contains the method get_move(board)
        wait: wait after every move?
        result:
        '''
        chess_board = chessBoard()
        count = 0
        max_count = chess_board.row_count * chess_board.col_count
        # player1 -> WHITE
        # player2 -> BLACK
        while count < max_count:
            i,j = player1.next_move(chess_board,chessBoard.WHITE)
            chess_board.move(i,j,chessBoard.WHITE)
            if wait1 != 0 and print_details:
                time.sleep(wait1)
            status = chess_board.get_status_after_move(i,j)
            if status != 0:
                print(status,"win")
                chess_board.print_board()
                return status

            i,j = player2.next_move(chess_board,chessBoard.BLACK)
            chess_board.move(i,j,chessBoard.BLACK)
            if wait2 != 0 and print_details:
                time.sleep(wait2)
            status = chess_board.get_status_after_move(i,j)
            if status != 0:
                print(status,"win")
                chess_board.print_board()
                return status

            if print_details:
                chess_board.print_board()
            count += 2


if __name__ == '__main__':
    gd = godVision()
    player1 = randomPlayer()
    player2 = randomPlayer()
    gd.play(player1,player2,0,0,True)
