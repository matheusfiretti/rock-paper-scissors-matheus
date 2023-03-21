import random
choice = int(input('Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lista = [rock, paper, scissors]
computer = random.choice(lista)
print(lista[choice])

if choice == 0:
    if computer == rock:
        print(rock)
        print('Empate')
    elif computer == paper:
        print(paper)
        print('Perdeu!')
    else:
        print(scissors)
        print('Ganhou!')
elif choice == 1:
    if computer == rock:
        print(rock)
        print('Ganhou!')
    elif computer == paper:
        print(paper)
        print('Empate')
    else:
        print(scissors)
        print('Perdeu!')
else:
    if computer == rock:
        print(rock)
        print('Perdeu!')
    elif computer == paper:
        print(paper)
        print('Ganhou!')
    else:
        print(scissors)
        print('Empate')