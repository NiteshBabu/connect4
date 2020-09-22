class Connect_4():
  def __init__(self):
    self.board = [[0 for i in range(7)] for i in range(6)]
    self.turn = 1
    self.bottom = [5 for i in range(7)]
    self.player_color = {1:'Y', 2:'R'}


  def insert_in_col(self, y, player):
    if self.bottom[y] < 0 or y > 6 or self.turn != player:
      return 'Invalid'

    if self.turn == 1:
      self.turn = 2
    else:
      self.turn = 1

    self.board[self.bottom[y]][y] = self.player_color[player]
    self.bottom[y] -= 1
    return (self.bottom[y]+1, y)



  def has_won(self, loc, color):
    x,y = loc
    # check horizontally 
    count = 0
    for i in range(len(self.board[0])):
      if self.board[x][i] == color:
        count += 1
      if count == 4:
        return True

    # check vertically
    count = 0
    for i in range(len(self.board)):
      if self.board[i][y] == color:
        count += 1
      if count == 4:
        return True
    
    # check diagonally
    count = 0
    for i in range(len(self.board)):
      if i == x:
        continue
      for j in range(len(self.board)):
        if j == y:
          continue
        if ((i+j) == (x+y) or (j-i) == (y-x)) and self.board[i][j] == color:
          count += 1
      
      if count == 4:
        return True

    return False


  def reset(self):
    self.__init__() 


