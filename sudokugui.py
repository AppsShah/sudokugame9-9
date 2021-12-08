import pygame
import pygame.font
import numpy
import sudoku
pygame.init()
txtx=50
txty=40
# creating window
W=650
H=600
xset=0
yset=0
count=0
clock=pygame.time.Clock()
image=pygame.image.load("rectangle.png")
font = pygame.font.SysFont(None,30)
fontbutton = pygame.font.SysFont(None,25)
display=pygame.display.set_mode((W,H))
selectx=-150
selecty=-150
countselected=0
#selected=True
#board of game
board=[
[2,3,0,4,1,5,0,6,8], 
[0,8,0,2,3,6,5,1,9],
[1,6,0,9,8,7,2,3,4], 
[3,1,7,0,9,4,0,2,5],
[4,5,8,1,2,0,6,9,7],
[9,2,6,0,5,8,3,0,1],
[0,0,0,5,0,0,1,0,2],
[0,0,0,8,4,2,9,0,3],
[5,9,2,3,7,1,4,8,6] ]
board2=[
[2,3,0,4,1,5,0,6,8], 
[0,8,0,2,3,6,5,1,9],
[1,6,0,9,8,7,2,3,4], 
[3,1,7,0,9,4,0,2,5],
[4,5,8,1,2,0,6,9,7],
[9,2,6,0,5,8,3,0,1],
[0,0,0,5,0,0,1,0,2],
[0,0,0,8,4,2,9,0,3],
[5,9,2,3,7,1,4,8,6] ]
# creating GUI grid
def draw(display):
    x=20
    y=20
    wid=60
    size=3
    for row in board:
        for col in board: 
            pygame.draw.rect(display,(0,0,0),(x,y,wid,wid),size)
            x=x+wid
        y=y+wid
        x=20
def texttoscreen(display,num,pos):
    f=font.render(num,False,(0,0,0))
    display.blit(f,pos)
def texttoscreen2(display,num,pos,color):
    f=fontbutton.render(num,False,color)
    display.blit(f,pos)
def textdraw(txtx,txty):
    for i in range(0,9):
        for j in range(0,9):
            temp=board[i][j]
            if temp!=0:
                texttoscreen(display,str(temp),(txtx,txty))
                txtx=txtx+60
            else:
                txtx=txtx+60
        txty=txty+60
        txtx=50
def select(display,x,y):
    pygame.draw.rect(display,(255,255,100),(x,y,60,60),0)  
gamerun=True
while gamerun:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gamerun=False
            if event.type==pygame.MOUSEBUTTONUP:
                if event.button==1:
                    xpos,ypos=pygame.mouse.get_pos()
                    if xpos>=570 and xpos<=634 and ypos>=100 and ypos<=164:
                        sudoku.sudokusolver(board)
                    if xpos>=570 and xpos<=634 and ypos>=200 and ypos<=264:
                        sudoku.sudokusolver(board)
                        file=open("save.txt",'w')
                        for i in range(0,9):
                            for j in range(0,9):
                                temp=board[i][j]
                                file.write(str(temp))
                                file.write(" ")
                            file.write("\n")
                        file.close()  
                    if xpos>=570 and xpos<=634 and ypos>=300 and ypos<=364:
                        sudoku.sudokusolver(board2)
                        for i in range(0,9):
                            for j in range(0,9):
                                if(board[i][j]==board2[i][j]):
                                    pass
                                else:
                                    count=count+1  
                        if(count==0):
                            print("true")
                        else:
                            print("false") 
                        print(count)    
                    if xpos>=10 and xpos<=560 and ypos >=20 and ypos<=560:
                        wastex=10
                        wastey=20
                        xset=(xpos-wastex)//60
                        yset=(ypos-wastey)//60
                        app=board[yset][xset]
                        if app==0:
                            selectx=(xset*60)+wastex+8
                            selecty=(yset*60)+wastey+1
                            #print("zero ",selectx,selecty)
                        else:
                            switch=False
                            #print("non zero")
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    board[yset][xset]=1
                if event.key==pygame.K_2:
                    board[yset][xset]=2
                if event.key==pygame.K_3:
                    board[yset][xset]=3
                if event.key==pygame.K_4:
                    board[yset][xset]=4
                if event.key==pygame.K_5:
                    board[yset][xset]=5
                if event.key==pygame.K_6:
                    board[yset][xset]=6
                if event.key==pygame.K_7:
                    board[yset][xset]=7
                if event.key==pygame.K_8:
                    board[yset][xset]=8
                if event.key==pygame.K_9:
                    board[yset][xset]=9 
                if event.key==pygame.K_RETURN:
                    sudoku.board2print()
                    #pass
                    #selected=False
        #display.fill((255,255,255))
        display.fill((255,255,255))
        select(display,selectx,selecty)
        draw(display)
        textdraw(txtx,txty)
        #remaintext(txtx,txty)
        display.blit(image,(570,100))
        display.blit(image,(570,200))
        display.blit(image,(570,300))
        texttoscreen2(display,"solver",(579,120),(0,0,0))
        texttoscreen2(display,"save",(579,220),(0,0,0))
        texttoscreen2(display,"check",(579,320),(0,0,0))
        clock.tick(60)
        pygame.display.update()
