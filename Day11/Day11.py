import art
import random
import os
start=input("Do you want to play Black Jack y or n ? \n")

endgame =1



cards=[11,2,3,4,5,6,7,8,9,10,10,10,
  11,2,3,4,5,6,7,8,9,10,10,10,
  11,2,3,4,5,6,7,8,9,10,10,10,
  11,2,3,4,5,6,7,8,9,10,10,10
  ]

'''check if the user pick two aces and calculate score''' 
def check_Ace(player1):
    score=0
    cards.remove(player1[0])
    cards.remove(player1[1])
     
    if (player1[0] + player1[1]) >21:
      score=12
      player1[0]=11
      player1[1]=1
    else:
      score=sum(player1)
    return score  

'''choose random card for the user or the computer'''    
def pickCard(cards,numofCard,player):
  newCards=random.sample(cards,numofCard)
  for card in newCards:
    player.append(card)
    cards.remove(card)
  return player

''' computer keep playing while his score less 17 '''
def playComputer(computer,cmpscore):
  while cmpscore<17:
    computer = pickCard(cards,1,computer)
    cmpscore=sum(computer)
  return computer

  



while (start != 'y' and start != 'n'  ):
     start=input("Please enter the right character!!!")
     

while (endgame):

  if start == "n":
     print("Ok Have a Nice Day!!!")
     endgame=0
  elif start=="y":
     player1=[]
     score=0
     computer=[]
     cmpscore=0
    

     cards=[11,2,3,4,5,6,7,8,9,10,10,10,
            11,2,3,4,5,6,7,8,9,10,10,10,
            11,2,3,4,5,6,7,8,9,10,10,10,
            11,2,3,4,5,6,7,8,9,10,10,10
           ]
     print(art.logo)
     #select player cards
     player1=pickCard(cards,2,player1)
     #check presence of two aces and calculate score
     score=check_Ace(player1)
     print(f"you got this cards: [{player1}] current score:{score}")
     #select computer cards
     computer=pickCard(cards,2,computer)
     #check presence of two aces calculate score 
     cmpscore=check_Ace(computer)

     print(f"Computer first Card: {computer[0]}")
     newcard=""
     while (newcard != 'n' and score<=21):
        newcard=input(f"Type y if you want get another card n if you stand: ")
        #player choose to pick another card
        if newcard == 'y':
           player1=pickCard(cards,1,player1)
           score=sum(player1)
           print(f"Your Cards: [{player1}] Your score:{score}") 
        #player choose to stand
        if score>=21 or newcard=='n':
          computer=playComputer(computer,cmpscore)
          cmpscore=sum(computer)

     print(f"Computer Cards: [{computer}] Computer score:{cmpscore}")    
     if score>21 and cmpscore>21:
      print("Both players went overboard Player 1 win !!!")
     elif score>21 and cmpscore<21:
      print("Computer win you Lose !!!")
     elif (score == 21 and cmpscore ==21) or (score==cmpscore):
      print ("It's a Draw !!!")
     elif score ==21 and (cmpscore >21 or cmpscore<21):
      print("You win BlackJack $$$")
     elif score > cmpscore and score<21:
      print("You win !!!")
     elif score<21 and cmpscore>21:
      print("You win !!!") 
     else:
      print("Computer win you Lose !!!")
      
  start=input("Do you want to play again y or n ? \n")
  if start == 'n':
    endgame=0
  os.system('cls')


       



           



        


       



        





     








  

