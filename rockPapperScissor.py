import random

#provide instruction to user for plya game 
def get_instruction():
    print()
    print()
    print("Instructions for Rock-Paper-Scissors : ")
    print()
    print("Rock crushes Scissors")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()



#play Game function
def play_game(player_int):
    
    if player_int.lower() == "rock":
            player_move = 0
        
    elif player_int.lower() == "paper":
            player_move = 1
        
    elif player_int == "scissor":
            player_move = 2

    #get computer move in ramdomly
    comp_move = random.randint(0, 2)

      #declaire the winner
    winner = rps_table[player_move][comp_move]

    print()
    print("The player choise "+str(player_move)+ " The computer choise "+str(comp_move))
    print()

    #choice the winner who are
    if winner == player_move:
        print("You Win")

    elif winner == comp_move:
        print("Computer Win")

    else:
        print("It is tie:")



#Rock paper scissor game play functoin
def rps():
    global game_map
    global  rps_table

    while True:
        print()
        print()
        print("\t\tCongratulation.....You Entered to plya game")
        print()
        print("\t\t-------------------------------------")
        print("\t\tMenu")
        print("\t\t-------------------------------------")
        print("\t\tEnter 'help' for intruction")
        print("\t\tEnter 'rock', 'paper' or 'scissor' to plya game ")
        print("\t\tEnter 'exit' to quit")

        print()

        #get plyar input
        player_int = input("Enter your move: ")

        if player_int.lower() == "help":
            get_instruction()
            continue
        
        elif player_int.lower() == "exit":
            break

        #player move  
        elif player_int in ("rock", "paper", "scissor"):
            play_game(player_int)  
        
        #when wrong input
        else:
            print("\t\tWRONG INPUT")
            continue
        
       







#intial step of game
game_map = {0:"rock", 1:"paper", 2:"scissor"}

# Win lose matrix
rps_table = [[-1,1,0],[1,-1,2],[0,2,-1]]

while True:

  print()
  print("This is rock paper scissor game!!!!")
  print("Enter 1 to plya Game")
  print("Enter 2 to Exit Game")
  print()

  try:
    choice = int(input("Enter your choice = "))
  except ValueError:
    print("wrong choise")
    continue

  if choice == 1:
    rps()
  
  elif choice == 2:
    break

  else:
    print("Wrong choice")
    break




