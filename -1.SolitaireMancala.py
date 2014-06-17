#Don't forget about https://class.coursera.org/principlescomputing-001/wiki/honor_code
#http://www.codeskulptor.org/#user34_YZPCJkIc44_17.py

"""
double zero project SolitaireMancala for principles of computing
"""
#zero project SolitaireMancala for principles of computing


class SolitaireMancala:
    """
    SolitaireMancala class
    """
    
    def __init__(self):
        """
        initialization function
        """
        self._board = [0]
    

    def set_board(self, configuration):
        """
        setting the board
        """
        self._board = list(configuration)
        return self._board
    

    def __str__(self):
        """
        return bord like string in reverse order
        """
        temp = list(self._board)
        temp.reverse()
        return str(temp)

    def get_num_seeds(self, house_num):
        """
        return number of seeds in seperate house
        """
        return self._board[house_num]
    

    def is_legal_move(self, house_num):
        """
        boolean function check is the move legal
        """
        if house_num == 0:
            return False   
        
        if house_num == self._board[house_num]:
            return True
        else:
            return False
    

    def apply_move(self, house_num):
        """
        applying the mive if it is legal
        """
        if self.is_legal_move(house_num):
            for temp_index in range(0,house_num):
                self._board[temp_index]+=1
                self._board[house_num]-=1
    

    def choose_move(self):
        """
        choose first legal move if it is illegal return 0
        """
        for temp_index in range(1, len(self._board)):
            if self._board[temp_index]==temp_index:
                return int(temp_index)
        return int(0)
    

    def is_game_won(self):
        """
        check is the game if finished by winning
        """
        for temp_index in range(1, len(self._board)):
            if self._board[temp_index]!=0:
                return False
        return True
      

    def plan_moves(self):
        """
        plan the moves for winning
        """  
        plan_moves_list = []
        temp = SolitaireMancala()
        temp.set_board(list(self._board))
        move = 0
        move = temp.choose_move()
        while move!=0:
            temp.apply_move(move)
            plan_moves_list.append(move)
            move = temp.choose_move()
        return plan_moves_list
            
            
import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())

