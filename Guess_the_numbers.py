'''
Created on Jun 24, 2021

@author: MUSHANDANA L
'''

'''
1.change the number range from 1 to 1000000
2.game should  ask us to guess a  mumber
3.Game should also give us clue of the number is higher or lower than the guess
3.inform if the player won 
'''

from random import randint

start =1

end=1000000

value=randint(start, end)

print("The computer choose a  number between ", start , "and ",end)

guess=None

while guess !=value:
    text=input("Guess the number:")
    guess=int(text)
    
    if guess<value:
        print("The number is higher")
    elif guess>value:
        print("The number is lower")

print("congratulation!!!! You  guessed the number...You won**")
    
    


