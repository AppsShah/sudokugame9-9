import numpy
count=[]
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
for i in range(0,9):
        for j in range(0,9):
            temp=board[i][j]
            if temp==0:
               count.append([i,j])
               #print(count)
t=[]
t.append([10,20])
sub=numpy.subtract(t,count)
print(sub)
if event.key==pygame.K_1:
                    keypress="1"
                if event.key==pygame.K_2:
                    keypress="2"
                if event.key==pygame.K_3:
                    keypress="3"
                if event.key==pygame.K_4:
                    keypress="4"
                if event.key==pygame.K_5:
                    keypress="5"
                if event.key==pygame.K_6:
                    keypress="6"
                if event.key==pygame.K_7:
                    keypress="7"
                if event.key==pygame.K_8:
                    keypress="8"
                if event.key==pygame.K_9:
                    keypress="9"
                if event.key==pygame.K_RETURN:
                    pass