import random

variants = [
  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choose = random.randint(0, 2)

if choose == computer_choose:
  print(variants[0])
  
  print("Computer chose:")
  print(variants[computer_choose])
  
  print("It's a draw")
elif choose == 0:
  print(variants[0])
  
  if computer_choose == 1:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You lose")
    
  elif computer_choose == 2:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You win!")
    
elif choose == 1:
  print(variants[1])
  
  if computer_choose == 0:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You win!")
    
  elif computer_choose == 2:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You lose")
    
elif choose == 2:
  print(variants[2])
  
  if computer_choose == 0:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You lose")
    
  elif computer_choose == 1:
    print("Computer chose:")
    print(variants[computer_choose])
    
    print("You win!")
    
else:
  print("Incorrect type")