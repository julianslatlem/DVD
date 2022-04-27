import pygame,random

pygame.init();pygame.display.init()
info=pygame.display.Info()

width,height=info.current_w,info.current_h
screen=pygame.display.set_mode((width,height))
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible(False)

dvd_width=int((height/6.4)*1.5);dvd_height=int((height/12.8)*1.5)
colors=["./colors/white.png","./colors/gray.png","./colors/blue.png","./colors/green.png",
"./colors/brown.png","./colors/pink.png","./colors/mint.png","./colors/pine.png",
"./colors/purple.png","./colors/rose-gold.png","./colors/aqua.png","./colors/gold.png"]
color=0

x=(width/2)-(dvd_width/2);y=(height/2)-(dvd_height/2)
xvel=random.randrange(int(height/80),int(height/64))/10;yvel=int(height/320)-xvel

up=False
down=False
left=False
right=False

friction=True
frictionAmount=0.005

clock=pygame.time.Clock()
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_f and friction==False:
                friction=True
            elif event.key==pygame.K_f and friction==True:
                friction=False
            if event.key==pygame.K_PLUS or event.key==pygame.K_KP_PLUS:
                frictionAmount+=0.001
            elif event.key==pygame.K_MINUS or event.key==pygame.K_KP_MINUS:
                frictionAmount-=0.001
            if event.key==pygame.K_SPACE and pygame.mouse.set_visible(True):
                pygame.mouse.set_visible(False)
            elif event.key==pygame.K_SPACE and pygame.mouse.set_visible(False):
                pygame.mouse.set_visible(True)
            if event.key==pygame.K_UP:
                up=True
            elif event.key==pygame.K_DOWN:
                down=True
            if event.key==pygame.K_RIGHT:
                right=True
            elif event.key==pygame.K_LEFT:
                left=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                up=False
            elif event.key==pygame.K_DOWN:
                down=False
            if event.key==pygame.K_RIGHT:
                right=False
            elif event.key==pygame.K_LEFT:
                left=False
                
    if up==True:
        yvel-=0.1
    if down==True:
        yvel+=0.1
    if right==True:
        xvel+=0.1
    if left==True:
        xvel-=0.1
        
    if friction==True:
        if yvel<=0:
            yvel+=frictionAmount
        else:
            yvel-=frictionAmount
        if xvel<=0:
            xvel+=frictionAmount
        else:
            xvel-=frictionAmount
        if yvel>15:
            yvel=15
        if yvel<-15:
            yvel=-15
        if xvel>15:
            xvel=15
        if xvel<-15:
            xvel=-15
    
    dvd=pygame.image.load(colors[color]).convert_alpha()
    dvd=pygame.transform.scale(dvd,(dvd_width,dvd_height))
    
    screen.fill((0,0,0))
    screen.blit(dvd,(x,y))
    
    x+=xvel
    y+=yvel
    if x<0 or x>(width-(dvd_width)):
        xvel*=-1;color+=1
    if y<0 or y>(height-(dvd_height)):
        yvel*=-1;color+=1
    if color>11:
        color=0

    pygame.display.update();pygame.display.flip()
    clock.tick(144)
    
pygame.quit;