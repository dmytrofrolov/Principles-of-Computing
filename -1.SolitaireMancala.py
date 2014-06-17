#Don't forget about https://class.coursera.org/principlescomputing-001/wiki/honor_code
#http://www.codeskulptor.org/#user34_YZPCJkIc44_11.py
#zero project SolitaireMancala for principles of computing


class SolitaireMancala:
    #initialization function
    def __init__(self):
        self.board = [0]
    
    #setting the board
    def set_board(self, configuration):
        self.board = list(configuration)
        return self.board
    
    #return bord like string in reverse order
    def __str__(self):
        temp = list(self.board)
        temp.reverse()
        return str(temp)
    
    #return number of seeds in seperate house
    def get_num_seeds(self, house_num):
        return self.board[house_num]
    
    #boolean function check is the move legal
    def is_legal_move(self, house_num):
        if house_num == 0:
            return False   
        
        if house_num == self.board[house_num]:
            return True
        else:
            return False
    
    #applying the mive if it is legal    
    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            for i in range(0,house_num):
                self.board[i]+=1
                self.board[house_num]-=1
    
    #choose first legal move if it is illegal return 0
    def choose_move(self):
        for temp_index in range(1, len(self.board)):
            if self.board[temp_index]==temp_index:
                return int(temp_index)
        return int(0)
    
    #check is the game if finished by winning
    def is_game_won(self):
        for temp_index in range(1, len(self.board)):
            if self.board[temp_index]!=0:
                return False
        return True
        
    #plan the moves for winning
    def plan_moves(self):
        plan_moves_list = []
        temp = SolitaireMancala()
        temp.set_board(list(self.board))
        move = 0
        move = temp.choose_move()
        while move!=0:
            temp.apply_move(move)
            plan_moves_list.append(move)
            move = temp.choose_move()
        return plan_moves_list
            
