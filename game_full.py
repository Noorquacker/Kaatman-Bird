#Kaatman Bird
#Revised 2019-01-11 16:28
import pygame, random, time, sys
print("Kaatman Bird")
pygame.init()
clock = pygame.time.Clock()
try:
    pygame.display.set_icon(pygame.image.load("zerotwo.png"))
    bird = pygame.image.load("kaatman.png")
    bird_dead = pygame.image.load("kaatmandie.png")
except:
    print("yo I can't find the game files")
    print("Exiting...")
    pygame.quit()
    sys.exit()
window = pygame.display.set_mode((720,720))
pygame.font.init()
pygame.display.set_caption('Kaatman Bird')
font, font2 = pygame.font.SysFont('Arial', 72), pygame.font.SysFont('Arial', 36)
title = font.render('Kaatman Bird', True, (0,0,0), None)
caption = font2.render('Press SPACE to Start', True, (0,0,0), None)
global start, vel, ypos, hscore, p1, p2, tscore, died
start = False
vel = 0
ypos = 300
hscore = 0
pipe = [720,random.randint(0,380)]
tscore = 0
died = False
while True:
    window.fill((120,120,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start == False:
                    ypos = 300
                    start = True
                vel = 7.
    if start:
        window.blit(bird,(50,ypos))
        ypos = ypos - vel
        vel = vel - 0.5
        pygame.draw.rect(window,(0,255,0),(pipe[0],0,50,pipe[1]))
        pygame.draw.rect(window,(0,255,0),(pipe[0],pipe[1]+300,50,720))
        window.blit(font2.render('Score: ' + str(tscore), True, (0,0,0), None),(10,10))
        pipe[0] = pipe[0] - 5
        if pipe[0] < -50:
            pipe[0] = 720
            pipe[1] = random.randint(0,380)
            tscore = tscore + 1
            if tscore > hscore:
                hscore = tscore
    else:
        if died:
            window.blit(bird_dead,(100,500))
        window.blit(title,(100,100))
        window.blit(caption,(100,300))
        window.blit(font2.render('High score - ' + str(hscore), True, (0,0,0), None),(100,400))
    if (pipe[0] < 164 and pipe[0] > 14) and (ypos+192 > pipe[1]+300 or ypos < pipe[1]):
        ypos = 528
    if ypos >= 528:
        ypos = 528
        caption = font2.render('You died', True, (0,0,0), None)
        start = False
        tscore = 0
        pipe[0] = 720
        died = True
    elif ypos < 0:
        ypos = 0
        vel = -abs(vel)
    clock.tick(60)
    if time.time() - int(time.time()) < 0.02 and int(time.time()) % 5 == 0:
        print("FPS: " + str(int(clock.get_fps())))
    pygame.display.flip()
