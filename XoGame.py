
# ==============
# =  1 || 2 ||  3 =   
# =  4 || 5 ||  6 =
# =  7 || 8 ||  9 =
# ==============
# [
# [0,1,2 ], row 1 += 1 
# [ 0,1,2], row 2 += 4 
# [ 0,1,2]] row 3 += 6

# ! You only need to add the win using r and we will be finished
# ? hello 
# * this is for green 
# todo you must do this 


from random import randint
from time import sleep

class XO:
  AllowedChars = ["X","O"]
  AllowedRange = range(1,10)
  def __init__(self , player2option=False) -> None:
        
        self.rows = [[1,2,3],[4,5,6],[7,8,9]]
        self.player = self.AllowedChars[0]
        self.pc = self.AllowedChars[1]
        self.Allowed = [1,2,3,4,5,6,7,8,9]
        self.player2option = player2option
        if player2option :
          self.player2 = self.AllowedChars[1]
  
  def start(self) : 
    try: 
      Player2 = input("Do You Want Player Two? (Y , N)").strip().upper()
      UserInputChoice = input("You want to be (X) or (O)").strip().upper()
      if Player2 == "Y": 
        self.player2 = True
        
      if UserInputChoice not in self.AllowedChars:
        print("please Enter X or O")
      
      elif UserInputChoice in self.AllowedChars:
        
        self.player = UserInputChoice 
        self.AllowedChars.remove(UserInputChoice)
        other = self.AllowedChars.pop(0)
        self.player2 = other 
        self.pc = other
        print(f"Starting the game you are the {self.player} and the Other is {self.pc}")
      else :
        return False
    
    except ValueError:
      print("Enter Right Value")
  
  # this funcion will print the game in termnal
  def print(self):
    row1 = self.rows[0]
    row2 = self.rows[1]
    row3 = self.rows[2]
    print(f"""
==============
=  {row1[0]} || {row1[1]} || {row1[2]}  =
=  {row2[0]} || {row2[1]} || {row2[2]}  =
=  {row3[0]} || {row3[1]} || {row3[2]}  =
==============""")
  
  
  # return row then index
  @staticmethod
  def convert(place):
    try: 
        if place > 6 : 
          return 2,(place % 6) -1
        elif place > 3 :
          return 1,(place % 3) -1
        elif place >= 1 :
          return 0,place - 1
    except :
      print("Please Enter integer number")

  def play(self, play,who):
    """this funcion will use th check funcion and convert function to play the round"""
    
    if who == "USER":
      player = self.player
    elif who == "PC" : 
      player = self.pc
    elif who== "P2": 
      player = self.player2
    if play  in self.Allowed :
      pos = XO.convert(play)
      if play in self.Allowed:
        index= pos[1]
        row_play = pos[0]
        self.rows[row_play][index] = player
        self.Allowed.remove(play)
        return True

    else : 
      print("bad Position")
      return False
  
  

  def CheckWin(self): 
    # X X X
    for row in self.rows:
        set1 = set(row)
        if self.PrintWinner(set1):
          return True
        
    # X
    # X
    # X
    for i in range(3):
        set1 = {self.rows[0][i] , self.rows[1][i], self.rows[2][i]}
        if self.PrintWinner(set1):
          return True
    # X   X
    #   X
    # X   X
    set1 = {self.rows[0][0],self.rows[1][1],self.rows[2][2]}
    set2 = {self.rows[0][2],self.rows[1][1],self.rows[2][0]}
    if self.PrintWinner(set1):
      return True
    if self.PrintWinner(set2):
      return True
    if len(self.Allowed) == 0:
      print("No One Won")
      return True
    
    
  def PrintWinner(self,set):
    if len(set) == 1 :
      if set.pop() == self.pc :
          if not self.player2option : 
            print("PC Won!")
            return True
          else: 
            print("Player2 Won!")
            return True
      else:
            print("Player1 Won!")
            return True

game = XO()
game.start()
game.print()

play = int(input("Player1: "))
while True : 
  while play not in game.Allowed:
    play = int(input("Place: "))
  game.play(play , "USER") 
  game.print()
  if game.CheckWin() : 
    print("Game End")
    break
  # Pc play 
  if not game.player2 : 
    print("Computer Playing....")
    sleep(.5)
    game.play( game.Allowed[randint(0,len(game.Allowed)-1 )] , "PC")
    game.print()
  else :
      play = int(input("Player2: "))
      while play not in game.Allowed:
        play = int(input("Player2: "))
      game.play(play , "P2") 
      game.print()  
  if game.CheckWin() : 
    print("Game End")
    break
  else : 
    play = int(input("Place: "))
  
  