import time 
import random 
print(' twenty one')
print(' turtles racing')
print(' snake')
input('enter your choice:')
print('prepare the game....')
time.sleep(3)
def calculate_score(cards):
    score = sum(cards)
    aces = cards.count(11)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score
def code():
  cards_choices=[2,3,4,5,6,7,8,9,10,11]
  card_1=random.choice(cards_choices)
  card_2=random.choice(cards_choices)
  card_3=random.choice(cards_choices)
  card_4=random.choice(cards_choices)

  player_cards=[]
  computer_cards=[]

  player_cards.append(card_1)
  player_cards.append(card_2)

  computer_cards.append(card_3)
  computer_cards.append(card_4)
  player_score=calculate_score(player_cards)
      

  print(f'your cards is: {player_cards}') 
  print(f' all: {player_score}')
  
  print(f'computer first card is: {computer_cards[0]}')

  while True:
    choice=input('do you want to choose another card?').lower()
    if choice=="y":
      new_card=random.choice(cards_choices)
      player_cards.append(new_card)
      player_score=calculate_score(player_cards)
      print(f'your cards is: {player_cards}') 
            
      print(f' all: {player_score}')
      
    else:
      break  
#نهاية اللوب

  computer_score=calculate_score(computer_cards)
  while computer_score < 17:
      choices=["y","n"]
      computer_choice=random.choice(choices)
      if computer_choice=="y":
        card_new=random.choice(cards_choices)
        computer_cards.append(card_new)
        
        continue 
      else:
        break
  computer_score=calculate_score(computer_cards)

  print(f'computer cards are: ({computer_cards}')
  print(f'all: {computer_score}')
  
  if player_score>21:
    print('you lose')
  elif computer_score>21:
    print('you win')
  elif player_score>computer_score:
    print('you win')
  elif computer_score>player_score:
    print('computer win')
  else:
    print('it is a tie')
    
code()
