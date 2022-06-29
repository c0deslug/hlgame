import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0
listA=[]
listB=[]
higher=0
gameOver=False


# generate random account:
# accountA = random.choice(data)
# accountB = random.choice(data)

def get_start_data():

  A_item = random.randint(0, 50)
  B_item = random.randint(0, 50)
  if B_item == A_item:
    B_item = random.randint(0, 50)
  else:
    pass


  for key in data[A_item].values():
    listA.append(key)
  for key in data[B_item].values():
    listB.append(key)

def get_more_data():
  listB = []
  #B_item = 0
  B_item = random.randint(0, 50)
  for key in data[B_item].values():
    listB.append(key)
  return listB

def is_higher(listA, listB):
  if listA[1] > listB[1]:
    higher = "A"
  else:
    higher = "B"
  return higher 


get_start_data()

while not gameOver:
  print(logo)
  print(f"Current score: {score}")
  print (f"Compare A: {listA[0]}, a {listA[2]} from {listA[3]}")

  print (vs)

  print (f"Against B: {listB[0]}, a {listB[2]} from {listB[3]}")

  user_guess = input("Who has more followers? Type 'A' or 'B': ")
  higher = is_higher(listA, listB)
  if user_guess == higher:
    score += 1
    if higher == "B":
      listA = listB
    listB=get_more_data()
    clear()
  else:
    print("You're wrong, over.")
    gameOver = True
  