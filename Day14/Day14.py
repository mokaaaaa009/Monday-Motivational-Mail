import art
import game_data
import random
import os
#Display art
print(art.logo)

def displayPersons(account,a):
  print(f"Compare {a}:{account['name']}, a {account['description']},from {account['country']}\n")
def checkAnswer(fp_follower,p_follower,choice):
  if fp_follower>p_follower:
    return choice=="a"
  elif fp_follower < p_follower:
    return choice=="b"  




myData = game_data.data
cnt=0
retry =""
#Generat random accounts
person=random.choice(myData)
while retry != 'n':
  firstperson=person 
  person=random.choice(myData)
  while person == firstperson:
    person=random.choice(myData)

    break
  #display choices to user
  displayPersons(firstperson,"A")
  print(art.vs)
  displayPersons(person,"B")


  choice =input("Who has more followers? Type 'A' or'B'").lower()
  ans=checkAnswer(firstperson['follower_count'],person['follower_count'],choice)
  if ans == True:
      cnt+=1
      print("You are right let's go for the next level")
  else:
      print(f"Sorry your answer is wrong your score is {cnt}. \n {firstperson['name']} followers is {firstperson['follower_count']}\n{person['name']} followers is {person['follower_count']}\n")
      retry=input("Press y if you want to play again n to exit : ")
  os.system('cls')
  



      
     



