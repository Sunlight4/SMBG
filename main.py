import pygame, easygui
pygame.init()
mixer = pygame.mixer
mixer.init()
music=mixer.music
screen=pygame.display.set_mode([640, 480])
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
fill=screen.fill
draw = blit
titlescreen=load("images/SuperMarioGalaxyTitle.png")
rosalina=load("images/Rosalina.png")
bowser=load("images/Bowser_Sprite_NSMBW.png")
run=1
pygame.display.set_caption("Super Mario Bros. Galaxy")
q=1
blit(titlescreen, [0,0])
blit(rosalina, [100, 300])
blit(bowser, [420, 300])
music.load("music/SkyStationGalaxy.ogg")
music.set_volume(1)
music.play(-1)
while run:
    flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
            q=1
        elif event.type==pygame.KEYDOWN and event.key==ord("x"):
            run=0

if q:pygame.quit()

