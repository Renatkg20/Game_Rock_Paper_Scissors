import pygame.examples.stars
import random as rm
# source: https://github.com/takluyver/pygame/blob/master/examples/stars.py
#pygame.examples.stars.main()
user_score = []
comp_score = []
count = 0
while count < 3:
    list1 = ["Rock", "Paper", "Scissors"]
    user_input = (input("Pls choose Rock, Paper, Scissors \n")).capitalize()
    user_comp = list1[rm.randrange(3)]
    if user_input == "Rock" and user_comp == "Scissors":
       user_score.append(1)
       count +=1
       print(user_comp)
    elif user_input == "Paper" and user_comp == "Rock":
       user_score.append(1)
       count +=1
       print(user_comp)
    elif user_input == "Scissors" and user_comp == "Paper":
       user_score.append(1)
       count +=1
       print(user_comp)
    elif user_input == user_comp:
       user_score.append(1)
       comp_score.append(1)
       count +=1
       print(user_comp)
    else:
       comp_score.append(1)
       count +=1
       print(user_comp)
if sum(user_score) > sum(comp_score):
    print(f"User Win {sum(user_score)}")
    

else:
  print(f"Computer Win {sum(comp_score)}")
   
 