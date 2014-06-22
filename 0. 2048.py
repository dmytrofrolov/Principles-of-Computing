#http://www.codeskulptor.org/#user34_83AdqGExHK_13.py
"""
Clone of 2048 game.
"""

import poc_2048_gui        
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_list = []
    line_len_const = len(line)
    for temp_index in range(0,len(line)):
        if line[temp_index]==0:
            line.remove(0)
            line.append(0)
    if len(line)<2:
        result_list = list(line)
    start_size = int(len(line))
    temp_index = 0
    while start_size!=0:
        
        if len(line)-temp_index > 1:
            if line[temp_index]==line[temp_index+1] and line[temp_index]>0:
                result_list.append(line[temp_index]+line[temp_index+1])
                line.pop(temp_index+1)
            else:
                result_list.append(line[temp_index])
        if len(line)>4:
            if len(line)-temp_index == 1:
                result_list.append(line[temp_index])
        start_size-=1
        temp_index+=1
    
    while len(result_list)<line_len_const:
        result_list.append(0)
    return result_list

print merge([16, 16, 16, 16, 16, 16])

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.main_cells = []
        temp_width = []
        for row in range (grid_width):
            temp_width.append(0)
            print row
        for col in range(grid_height):
            self.main_cells.append(list(temp_width))
            print col
            
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.main_cells = []
        temp_width = []
        for row in range (self.grid_width):
            temp_width.append(0)
            print row
        for col in range(self.grid_height):
            self.main_cells.append(list(temp_width))
            print col
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return self.main_cells

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # self.main_cells [col(grid_height)][row(grid_width)]
        key_dir = list (OFFSETS[direction])
        temp_list = []
        if key_dir[0]==0:
            for temp_index in range(self.grid_height):
                if key_dir[1]>0:
                    self.main_cells[temp_index] = merge(self.main_cells[temp_index])
                else:
                    temp_list = self.main_cells[temp_index]
                    temp_list.reverse()
                    temp_list2 = merge(temp_list)
                    temp_list2.reverse()
                    self.main_cells[temp_index] = temp_list2
        else:
            for temp_index2 in range(self.grid_width):
                for temp_index in range(self.grid_height):
                    temp_list.append(self.main_cells[temp_index][temp_index2])
                print temp_list
                if key_dir[0]<0:
                    temp_list.reverse()
                temp_list_end = merge(temp_list)
                if key_dir[0]<0:
                    temp_list_end.reverse()
                for temp_index in range(self.grid_height):
                    self.main_cells[temp_index][temp_index2] = temp_list_end[temp_index]
  
                temp_list = []
        self.new_tile()
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        free_cells = 0
        # self.main_cells [col(grid_height)][row(grid_width)]
        for col in range(0,self.grid_height):
            for row in range(0,self.grid_width):
                if self.main_cells[col][row]==0:
                    free_cells+=1
        if free_cells>0:
            random_imov = random.randrange(0, 10)
            random_col = random.randrange(0, self.grid_height)
            random_row = random.randrange(0, self.grid_width)
            while self.main_cells[random_col][random_row]!=0:
                random_col = random.randrange(0, self.grid_height)
                random_row = random.randrange(0, self.grid_width)
            
            if random_imov==0:
                self.main_cells[random_col][random_row] = 4
            else:
                self.main_cells[random_col][random_row] = 2

        
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.main_cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.main_cells[row][col]
 

    
    

poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
