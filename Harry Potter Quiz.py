import streamlit as st
st.title('Harry Potter House Quiz')


slytherin = 0 
gryffindor = 0
ravenclaw = 0
hufflepuff = 0

print('Q1) Do you like Dawn or Dusk? ')
print('1) Dawn')
print('2) Dusk')
answer = int(input('Enter your answer (1-2): '))
if answer == 1:
  gryffindor +=1
  ravenclaw +=1 

elif answer == 2:
  hufflepuff +=1 
  slytherin +=1

else:
  print('Wrong Input') ()

print('Q2) When I`m dead, I want people to remember me as: ')
print('1) The Good ')
print('2) The Great ')
print('3) The Wise ')
print('4) The Bold ')
answer1 = int(input('Enter your answer (1-4): '))

if answer1 == 1:
  hufflepuff +=2 
elif answer1 == 2:
  slytherin +=2 
elif answer1 == 3:
  ravenclaw +=2 
elif answer1 == 4:
  gryffindor +=2
else:
  print('Wrong Input! ')


print('Q3) Which kind of instrument most pleases your ear? ')
print('1) The violin ')
print('2) The trumpet ')
print('3) The piano ')
print('4) The drum ')
answer2 = int(input('Enter your answer (1-4): '))

if answer2 == 1:
  slytherin +=4 
elif answer2 == 2:
  hufflepuff +=4
elif answer2 == 3:
  ravenclaw +=4
elif answer2 == 4:
  gryffindor +=4 
else:
  print('Wrong Input! ')

print('Gryffindor:', gryffindor)
print('Slytherin:', slytherin )
print('Ravenclaw:', ravenclaw)
print('Hufflepuff:', hufflepuff)

print('')

print('The Winner is...: ')
if (gryffindor >= slytherin) and (gryffindor >= ravenclaw) and (gryffindor >= hufflepuff):
  print('Gryffindor!')
elif (slytherin >= gryffindor) and (slytherin >= ravenclaw) and (slytherin >= hufflepuff):
  print('Slytherin!')
elif (ravenclaw >= gryffindor) and (ravenclaw >= slytherin) and (ravenclaw >= hufflepuff):
  print('Ravenclaw!')
elif (hufflepuff >= gryffindor) and (hufflepuff >= slytherin) and (hufflepuff >= ravenclaw):
  print('Hufflepuff!')
else:
  print('It\'s a Tie!')
