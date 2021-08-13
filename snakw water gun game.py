import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp  =='snake':
     if you =='water ':
      return False
    elif you=='gun':
       return True
    elif comp =='water':
       if you =='gun':
           return False
       elif you== 'snake':
           return True
       elif comp =='gun':
           if you=='snake':
             return False
           elif you=='water':
               return True
           
       print("computer turn: snake water or gun")
  
randno = random.randint (1, 3)
if randno == 1 :
     comp = 'snake' 
elif randno ==2:
    comp='water'
elif randno ==3:
    comp = 'gun'
    
you = input("player 2 turn: snake water or gun : ")
a = gamewin(comp, you)
if a== None :
        print("the game is tie")
elif a:
       print("you win")
else :
    print("you lose")
    


               