import pygame
import time
import random
pygame.init()
width=500
height=500
dis=pygame.display.set_mode((width,height))
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
clk=pygame.time.Clock();
fstyle=pygame.font.SysFont("Arial",50)
sstyle=pygame.font.SysFont("Times New Roman",30)
def score(s):
    
    smesg=sstyle.render("SCORE-"+str(s),True,white)
    dis.blit(smesg,[0,height-50])
def snake(slist):
    for x in slist:
        pygame.draw.circle(dis,blue,[x[0],x[1]],10)
        #print("x0 x1",x[0],x[1])
def display(msg,color):
    message=fstyle.render(msg,True,color)
    dis.blit(message,[width//2-120,height//2-80])
def gamecontd():
    xc=0
    yc=0
    slist=[]
    length=1
    x=width//2
    y=height//2
    speed=10
    gameOver=False
    gameClose=False
    fx=round(random.randrange(0,width-10)/10)*10
    fy=round(random.randrange(0,width-10)/10)*10
    while gameOver is not True:
        while gameClose is True:
            dis.fill(black)
            display("Press c to continue",red)
            score(length-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        gamecontd()
                elif event.type==pygame.QUIT:
                    gameOver=True
                    gameClose=False
        for event in pygame.event.get():
        
            if event.type==pygame.QUIT:
                gameOver=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    xc=-10
                    yc=0
                elif event.key==pygame.K_RIGHT:
                    xc=10
                    yc=0
                elif event.key==pygame.K_DOWN:
                    yc=10
                    xc=0
                elif event.key==pygame.K_UP:
                    yc=-10
                    xc=0
        if x>=width or x<0 or y>=height or y<0:
                gameClose=True
        x+=xc
        y+=yc
        dis.fill(black)
        pygame.draw.circle(dis,red,[fx,fy],10)
        shead=[]
        shead.append(x)
        shead.append(y)
        slist.append(shead)
        #print (len(slist),length)
        if len(slist) > length:
            #print ("slist[0]",slist[0])
            del slist[0]
            #print ("slist[0]",slist[0])
        for i in slist[:-1]:
            #print ("slist[x]",slist[x])
            if i==shead:
                print ("shead",shead)
                gameClose=True
        snake(slist)
        score(length-1)
        pygame.display.update()
        if x==fx and y==fy:
            fx=round(random.randrange(0,width-10)/10)*10
            fy=round(random.randrange(0,width-10)/10)*10
            length+=1
        pygame.display.update()
        clk.tick(speed)
#display("GAME OVER",red)
#pygame.display.update()
#time.sleep(2)
    pygame.quit()
gamecontd()
