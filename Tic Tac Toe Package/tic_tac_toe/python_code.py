class tictactoe:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.moves = [[0]*3 for x in range(3)]
        self.player_pos = [["f"]*3 for x in range(3)]
        self.last_player = player2
        self.printall()
        self.game = 0
        
            
        
    
    def make_move(self,x,y,player_n):
        if(self.game == 1):
            print("Game finished {} won".format(self.last_player))
            return None
        
        if(self.last_player == player_n):
            print("It is other player's turn")
            return None
        
            
        if (self.moves[x][y]):
            print("Can't make that move.",end = ' ')
            print("There is {} there".format(self.player_pos[x][y]))
            return None
        else:
            self.moves[x][y] = 1
            self.last_player = player_n
        
        if (player_n == self.player1):
            self.player_pos[x][y] = 'X'
        else:
            self.player_pos[x][y] = "O"
        self.printall()
        self.check_game(player_n)
    
    def printall(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.player_pos[i][j],sep = ' ',end = ' ')
            print('',end = '\n')
        print('',end = '\n')
            
    
    def check_game(self,player):
        if (player == self.player1):
            op = "X"
        else:
            op = "O"
        
        for ind in range(0,3):
            if ((self.player_pos[ind][0] == op) & \
            (self.player_pos[ind][1] == op) & (self.player_pos[ind][2] == op)):
                self.game = 1
            elif ((self.player_pos[0][ind] == op) & \
            (self.player_pos[1][ind] == op) & (self.player_pos[2][ind] == op)):
                self.game = 1
        
        if((self.player_pos[0][0] == op) &  \
        (self.player_pos[1][1] == op) & (self.player_pos[2][2] == op)):
            self.game = 1
        elif((self.player_pos[0][2] == op) &  \
        (self.player_pos[1][1] == op) & (self.player_pos[2][0] == op)):
            self.game = 1
        
        if self.game == 1:
            print("Game finished {} won".format(player))
            print("Type game = tictactoe('Player1','Player2') if you want to restart")
            exit
        else:
            return None
        