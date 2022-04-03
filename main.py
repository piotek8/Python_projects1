""" from time import sleep
for my_box in [10,9,8,7,6,5,4,3,2,1,0]:
  print(my_box) 
  if my_box == 2: 
    sleep(1)
  if my_box == 1: 
    sleep(1)
  if my_box == 0: 
    sleep(1)  
  sleep(1)
print ('boom')"""


 
'''
//////////////////////////////////
print ('1')
sleep (0.1)
print ('2') 
sleep (0.1)
print ('3')
sleep (0.1)
print ('4')
sleep (0.1)
print ('5')
sleep (0.1)
print ('6')
sleep (0.1)
print ('7')
sleep (0.1)
print ('8')
sleep (0.1)
print ('9')
sleep (0.1)
print ('10')
sleep (0.025)
print ('START') 
//////////////////////////////////
 '''

'''
from time import sleep
for my_box in [10,9,8,7,6,5,4,3,2,1,0]:
  print(my_box)  
  if my_box == 2:
    sleep (1.5)
print ('boooom')
//////////////////////////////////
'''

'''
x = input ('Podaj imie : ')
print ('Podane imie to')
print (x)
 
 
NIE DZIALA NIE DZIALA NIE DZIALA
  
Player_choice1 = input ('Player 1 give your choice: ')
Player_choice2 = input ('Player 2 give your choice: ')
if Player_choice1 == 'paper' :   
  if Player_choice2 == 'stone':
    print ('Player 1 : wins')  
if Player_choice1 == 'paper':      
  if Player_choice2 == 'scissors'
    print ('Player 1 : loses')
    print ('Player 2 : wins')
if Player_choice1 == 'paper':      
  if Player_choice2 == 'paper'
    print ('Player 1 : draw')
    print ('Player 2 : draw')
if Player_choice1 == 'stone':      
  if Player_choice2 == 'paper'
    print ('Player 1 : loses')
    print ('Player 2 : wins')
if Player_choice1 == 'stone':      
  if Player_choice2 == 'scissors'
     print ('Player 1 : wins')
     print ('Player 2 : loses')
if Player_choice1 == 'stone':      
  if Player_choice2 == 'stone'
     print ('Player 1 : draw')
     print ('Player 2 : draw')
if Player_choice1 == 'scissors':      
  if Player_choice2 == 'stone'
     print ('Player 1 : loses')
     print ('Player 2 : wins')
if Player_choice1 == 'scissors':      
  if Player_choice2 == 'paper'
     print ('Player 1 : wins')
     print ('Player 2 : loses')
if Player_choice1 == 'scissors':      
  if Player_choice2 == 'scissors'
     print ('Player 1 : draw')
     print ('Player 2 : draw')
Player_choice1 = input ('Player 1 give your choice: ')
Player_choice2 = input ('Player 2 give your choice: ')
if Player_choice1 == 'scissors' and Player_choice2 == 'scissors':
     print ('Player 1 : draw Player 2 : draw ')
     print ('Player 2 : draw')
NIE DZIALA NIE DZIALA NIE DZIALA
  pojemnik = 4
  
  if pojemnik == 4:
      print ('dziala dla 4')
  
  if pojemnik == 5:
      print ('dziala dla 5')


Player_choice1 = input ('Player 1 give your choice: ')
Player_choice2 = input ('Player 2 give your choice: ')

if player_choice1 == 'paper' :
  if player_choice2 == 'stone' :
    print('Player1 win')

elif player_choice1 == 'stone':
  if player_choice2 == 'scissors':
    print('Player1 win')

elif player_choice1 == 'scissors' :
  if player_choice2 == 'paper':
    print('Player1 win')

else: 
  print('Player2 win')





Player_choice1 = input ('Player 1 give your choice: ')
Player_choice2 = input ('Player 2 give your choice: ')

if Player_choice1 == 'paper' and Player_choice2 == 'stone' or Player_choice1 == 'stone' and Player_choice2 == 'scissors' or Player_choice1 == 'scissors' and Player_choice2 == 'paper':
    print('Player1 win')
elif Player_choice1 == Player_choice2:
  print('Draw')
else: print('Player2 win')

'''
import getpass

Player_result1 = 0
Player_result2 = 0

options = ['paper', 'stone', 'scissors']

while Player_result1 != 3 and Player_result2 != 3:
  
  The_players_choice_is_correct = True
  while The_players_choice_is_correct:
    Player_choice1 = getpass.getpass('Player 1 give your choice: ' )
    if Player_choice1 in options:
      The_players_choice_is_correct = False

  The_players_choice_is_correct = True
  while The_players_choice_is_correct :
    Player_choice2 = getpass.getpass('Player 2 give your choice: ')
    if Player_choice1 in options:
      The_players_choice_is_correct = False

if Player_choice1 == 'paper' and Player_choice2 == 'stone' \
or Player_choice1 == 'stone' and Player_choice2 =='scissors' \
or Player_choice1 == 'scissors' and Player_choice2 == 'paper' :
    print('Player1 win')
    Player1_result += 1
elif Player_choice1 == Player_choice2:
  print('Draw')
else: 
  print('Player 2 win')
  Player2_result += 1


if Player_result1 > Player_result2:
  print ('The Player 1 wins whole game')
else:
  print ('The Player 2 wins whole game')