import copy
from operator import truediv


'''
import sys
import pygame
from pygame.locals import *


pygame.init()   


#초당 프레임
FPS = 30
FramePerSec = pygame.time.Clock()

#color
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  
RED = (255, 0, 0)   
GREEN = (0, 255, 0)

GameDisplay = pygame.display.set_mode((640, 440))
GameDisplay.fill(WHITE) #흰색 배경
pygame.display.set_caption("pygame exampleㅇ??")

#draw a line, circle etc..
pygame.draw.circle(GameDisplay, BLACK, (100,50), 30)


pygame.draw.line(GameDisplay,BLUE,(200,20),(180,60))
pygame.draw.line(GameDisplay,BLUE,(200,20),(220,60))
pygame.draw.line(GameDisplay,BLUE,(180,60),(220,60))

pygame.draw.rect(GameDisplay,RED,(300,20,50,50),2)

pygame.draw.ellipse(GameDisplay,GREEN,(400,20,80,50),2)




#event loop

running  = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    FramePerSec.tick(FPS)
    


#pygame quit
pygame.quit()

'''



# tic tac toe



s = [[0 for j in range(3)] for i in range(3)]

s[0][1] = 'X'
s[0][2] = 'O'
s[1][0] = 'O'
s[1][1] = 'X'
s[1][2] = 'X'
s[2][0] = 'X'
s[2][2] = 'O'

#print(s)

#who's turn??
#first = X
def player(s):
    x_count= o_count = 0
    for i in range(3):
        for j in range(3):
            if s[i][j] == 'X':
                x_count += 1
            elif s[i][j] == 'O':
                o_count += 1
    
    if (x_count == 0) and (o_count == 0):
        return 'X'
    elif x_count == o_count:
        return 'X'
    else: return 'O'


# print(player(s))

def actions(s):
    turn = player(s)
    sol = []
    #temp = s
    arr = [[0 for j in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            arr = [[0 for j in range(3)] for i in range(3)]
            #temp = copy.deepcopy(s)  #deep copy!!
            if s[i][j] == 0: #empty!
                arr[i][j] = turn
                sol.append(arr)
    
    return sol

# print(actions(s))


def result(s, a):
    temp = copy.deepcopy(s)
    for i in range(3):
        for j in range(3):
            if a[i][j] == 'X':
                temp[i][j] = 'X'
                #return temp
            elif a[i][j] == 'O':
                temp[i][j] = 'O'
                #return temp
    
    return temp 

# print("s :", s)
# a = actions(s)
# print("a :", a[0])

# print(result(s, a[0]))




def terminal(s):
    #row
    r1 = [(0, 0), (0, 1), (0, 2)]
    r2 = [(1, 0), (1, 1), (1, 2)]
    r3 = [(2, 0), (2, 1), (2, 2)]
    #column
    c1 = [(0, 0), (1, 0), (2, 0)]
    c2 = [(0, 1), (1, 1), (2, 1)]
    c3 = [(0, 2), (1, 2), (2, 2)]
    #diagonal
    d1 = [(0, 0), (1, 1), (2, 2)]
    d2 = [(2, 0), (1, 1), (0, 2)]
    
    terminate = [r1, r2, r3, c1, c2, c3, d1, d2]
    
    cnt = 0
    for i in range(3):
        for j in range(3):
            if s[i][i] == 'O' or s[i][j] == 'X':
                cnt += 1
    
    if cnt == 9: #FULL!!
        return True

    arr = []
    for i in range(3):
        for j in range(3):
            if s[i][j] == 'O':
                arr.append((i, j))
    
    for i in range(len(terminate)):
        cnt = 0
        ter = copy.deepcopy(terminate[i])
        for j in arr:
            for k in ter:
               if j == k:
                   cnt += 1
                   
        if cnt == 3:
            return True
    
    
    
    arr = []
    for i in range(3):
        for j in range(3):
            if s[i][j] == 'X':
                arr.append((i, j))
    
    for i in range(len(terminate)):
        cnt = 0
        ter = copy.deepcopy(terminate[i])
        for j in arr:
            for k in ter:
               if j == k:
                   cnt += 1
        
        if cnt == 3:
            return True
    
    
    
    return False
    
# s = [['X', 0, 0], ['O', 'X', 0] , ['X', 'O', 'X']]
# print(terminal(s))

def utility(s): #X win : return 1 , O win : return -1, tie : return 0
    #row
    r1 = [(0, 0), (0, 1), (0, 2)]
    r2 = [(1, 0), (1, 1), (1, 2)]
    r3 = [(2, 0), (2, 1), (2, 2)]
    #column
    c1 = [(0, 0), (1, 0), (2, 0)]
    c2 = [(0, 1), (1, 1), (2, 1)]
    c3 = [(0, 2), (1, 2), (2, 2)]
    #diagonal
    d1 = [(0, 0), (1, 1), (2, 2)]
    d2 = [(2, 0), (1, 1), (0, 2)]
    
    terminate = [r1, r2, r3, c1, c2, c3, d1, d2]

    arr = []
    for i in range(3):
        for j in range(3):
            if s[i][j] == 'O':
                arr.append((i, j))
    
    for i in range(len(terminate)):
        cnto = 0
        ter = copy.deepcopy(terminate[i])
        for j in arr:
            for k in ter:
               if j == k:
                   cnto += 1
                   #print(cnto)
        
        if cnto == 3:
            return -1
    
    
    
    arr = []
    for i in range(3):
        for j in range(3):
            if s[i][j] == 'X':
                arr.append((i, j))
    
    for i in range(len(terminate)):
        cntx = 0
        ter = copy.deepcopy(terminate[i])
        for j in arr:
            for k in ter:
               if j == k:
                   cntx += 1
    
        if cntx == 3:
            return 1
    
    return 0  #tie

'''
print("\n\n\n")
s = [['O', 0, 'X'], ['O', 'X', 0],['X', 'O','X']]
print("util:" , utility(s))
print(terminal(s))
s = [['O', 'X', 'X'], ['X', 'O', 0],['O', 'X','O']]
print("util:" , utility(s))
print(terminal(s))
'''

def max_value(s):
    if terminal(s):
        return utility(s)
    
    v = float('-inf')
    for action in actions(s):
        v = max(v, min_value(result(s, action)))
    
    return v

def min_value(s):
    if terminal(s):
        return utility(s)
    
    v = float('inf')
    for action in actions(s):
        v = min(v, max_value(result(s, action)))
    
    return v

def minimax(s):
    if terminal(s):
        return None
    
    if player(s) == 'X':
        v = float("-inf")
        for action in actions(s):
            k = min_value(result(s, action))
            if k > v:
                v = k
                a = action
    else: # player = 'O'
        v = float('inf')
        for action in actions(s):
            k = max_value(result(s, action))
            if k < v:
                v = k
                a = action #2D-array
    
    return a

                          
        
        
        

def initial():
    return [[0 for j in range(3)] for i in range(3)]