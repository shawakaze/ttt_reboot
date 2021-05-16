# -*- coding: utf-8 -*-
"""
    Mark Shawa 
    Intelligent Systems : Assignemnet 2
    tic-tac-toe
    
    
    Key:
    The e's mean empty, x's mean crosses and the o's mean noughts
    Using a matrix to make the board, here we will use sympy for e's, x's & o's.
    
    x |   | o
  -------------
      | x |
  -------------
    o |   | x 
    
    
    
"""
import sympy as syp
import random,sys

print("This version of tictactoe learns from its own mistakes.\nThe more you play with it the smarter it gets.\n","Key to this game is\n",syp.Matrix([[0,1,2],[3,4,5],[6,7,8]]),"\nThe e's represent empty slots.\n","The human plays crosses after the cpu has played, \n\n\t GOODLUCK!!")


#_________________________________________________________________________________
#
#                           The globals come first
#_________________________________________________________________________________

x,o,e = syp.Symbol('x'),syp.Symbol('o'),syp.Symbol('e')
#------- game key,, essential feature    
game_key={1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}


# The first part of the program is dedicated to making the program learn using lists and 
# all possible win variations.
def play_field():
    return syp.Matrix([[e,e,e],[e,e,e],[e,e,e]])
    
# my random number generator
def myrand():
    return random.randint(0,8)
    
def win_condition(A):
    for i in range(3):    
        if A[i,0]==A[i,1]==A[i,2]==o:
            return 1
        if A[0,i]==A[1,i]==A[2,i]==o:
            return 1
    if A[0,0]==A[1,1]==A[2,2]==o or A[0,2]==A[1,1]==A[2,0]==o:
        return 1


def loss_condition(A):
    for i in range(3):    
        if A[i,0]==A[i,1]==A[i,2]==x:
            return 1
        if A[0,i]==A[1,i]==A[2,i]==x:
            return 1
    if A[0,0]==A[1,1]==A[2,2]==x or A[0,2]==A[1,1]==A[2,0]==x:
        return 1
      
def game_engine():
    # Board, is a matrix
    A = play_field()
    wins=[]
    exit_status = False
   
    while not exit_status:
   
#---------- cpu1 input --------------------------------------------        
        
        i = myrand()
        while i in wins:
            i = myrand()
        wins.append(i)
        A[game_key.values()[i]]=o
            
#-----------  cpu2 input -----------------------------
        j = myrand()
        while j in wins:
            j = myrand()
        wins.append(j)
        A[game_key.values()[j]]=x
              
#--------- decision --------------------------
        # player 1 or cpu 1 will always win this game 
        if win_condition(A) == 1:
            exit_status = True
            return wins
        
        # loss was used in the training part
        elif loss_condition(A) == 1:
            return "loss"
            exit_status = True
            
         # draw condition   
        elif len(wins) >= 8:
            exit_status = True
            return "draw"
        
        
def intelligence_engine():
    learning_list = []
    print("Loading Intelligence, please wait patiently.\n")
    for i in range(2500):
        l = game_engine()
        while len(l) == 9: # for obvious reasons here the learning lists must be long = hard enough
            l = game_engine()
        if type(l) == list:
            learning_list.append(l)
    return learning_list
    
###############################################################################################
#
#                       training done now you play 
#
###############################################################################################
# now we try cpu vs human

# to calculate all previous moves and future moves this function is needed

# iq - is the master list
# i - is the move by the cpu
# j - is the move made by the mortal/human (hehehehe)
# n - is the current move number

def prev(iq,i,j,n):
    for k in range(len(iq)):
        z = myrand()
        while z == i or z == j:
            z = myrand()
        if i == iq[k][n-2] and j == iq[k][n-1]:# and len(iq[k])>=n+1:
            return iq[k][n]
        else:
            return z
#------------------------------------------------------------------------------------
# counter for counting number of moves 
def gc(i): 
    i+=1
    return i 
    
#-----------------------------------------------------------------------------------
# Here the rewarding scheme is by removal weak strategies from the super list
# defined is a function, to do just that.
#-----------------------------------------------------------------------------
def reward_by_removal(a,b):
    b.remove(a)
    return b

#-----------------------------------------------------------------------------------
# cpu game-engine
#-----------------------------------------------------------------------------------
def cpu(iq,i,j,n):
    if n==1 and i == j: return j
    return prev(iq,i,j,n)
    
#------------------------------------------------------------------------------------
#   user game-engine
#------------------------------------------------------------------------------------        
def usr(aux1):
    j = input("Please enter valid move:")
    while j in aux1:
        j = input("Please!! enter a valid move:")
    return j

####################################################################################
#
#       the main event
#
###################################################################################
def play():
    exit_status = False

    A = play_field()
    # number of moves played
    n = 0 
    j = myrand()
    i=j
    iq=intelligence_engine()
    print("\nIntelligence vagueness",len(iq))
    aux1 = []
    while not exit_status:

        n=gc(n)                
        i = cpu(iq,i,j,n)
        while i in aux1:
            i = cpu(iq,i,j,n)    
        aux1.append(i)         
        A[game_key.values()[i]]=o
        print(A)
        
        #n=gc(n)
        j = usr(aux1)
        aux1.append(j)
        A[game_key.values()[j]]=x
        
        if win_condition(A) == 1:
            usr_in = input("I win \n Continue?[1/0]:\t")
            if usr_in == 0:
                exit_status = True
                print("Goodbye")
            if usr_in == 1:
                print("please wait for program update\n checking for pattern",aux1)
#-----------------------------------------------------------------------------------------------                
### Warning , this is the trickiest part of this program do not change this                   
                temp_ex = False
                k = 0
                while k in range(len(iq)) and not temp_ex:
                    if iq[k][:len(aux1)]==aux1:
                        print("Updating I.Q")
                        iq.pop(k)
                        temp_ex = True
                    else:
                        k=k+1
###################################################################################################
                print("\nIntelligence sharpness",len(iq))
                n = 0
                A = play_field()
                j = myrand()
                i = j
                aux1=[]
                
        
        if loss_condition(A) == 1:
            usr_in = input("You win \n Continue?[1/0]:\t")
            if usr_in == 0:
                exit_status = True
                print("Goodbye")
            if usr_in == 1:
                print("please wait for program update\n checking pattern",aux1)   
#-----------------------------------------------------------------------------------------------------
# Warning , this is the trickiest part of this program do not change this                   
                temp_ex = False
                k = 0
                while k in range(len(iq)) and not temp_ex:
                    if iq[k][:len(aux1)]==aux1:
                        print("Updating I.Q")
                        iq.pop(k)
                        temp_ex = True
                    else:
                        k=k+1
###################################################################################################
                    
                print("Intelligence sharpness",len(iq))
                n = 0
                A = play_field()
                j = myrand()
                i = j
                aux1=[]
                
        elif n>5:
            print("Draw\n Better luck next time")
            exit_status = True
                
    if exit_status == True: # Just making sure it exits
        return sys.exit()

def main(): # main function could load more modules
     play()
     
main()
