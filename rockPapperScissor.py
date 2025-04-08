import random
randomnum = random.random()
if (randomnum > 0.0 and randomnum <= 1/3 ):
  computerchoice = "rock"
elif (randomnum > 1/3 and randomnum <= 2/3):
  computerchoice = "paper"
elif (randomnum > 2/3 and randomnum < 1):
  computerchoice = "scissor"

yourscore = 0
computerscore = 0

while(True):
  user = input("Enter your choice: ")
  if user in ('scissor', 'paper', 'rock'):      
      if (user == computerchoice):
        print('You chose '+user+' Compuer chose '+computerchoice)
        print("You tie")
        print('Your score '+str(yourscore)+' Computer score '+str(computerscore))

      elif ((user == 'rock' and computerchoice == 'scissor') or 
            (user == 'paper' and computerchoice == 'rock') or
            (user == 'scissor' and computerchoice == 'paper')) :
        yourscore += 1    
        print('You chose '+user+' Compuer chose '+computerchoice)
        print('You win')
        print('Your score '+str(yourscore)+' Computer score '+str(computerscore))

      else:
        computerscore += 1
        print('You chose '+user+' Compuer chose '+computerchoice)
        print('You lost')
        print('Your score '+str(yourscore)+' Computer score '+str(computerscore))

      
      game = input("\nIf you want to escape press n, to continue press any key. ")
      if (game == 'n'):
        break

  else:
    print("\nEnter correct name.\n")
