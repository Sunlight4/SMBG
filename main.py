import pygame, easygui
pygame.init()
mixer = pygame.mixer
mixer.init()
music=mixer.music
music.load("music/Titles/SkyStationGalaxy.ogg")
music.set_volume(1)
music.play(-1)
screen=pygame.display.set_mode([640, 480])
blit=screen.blit
flip=pygame.display.flip
load=pygame.image.load
fill=screen.fill
draw = blit
titlescreen=load("images/SuperMarioGalaxyTitle.png")
rosalina=load("images/Rosalina.png")
bowser=load("images/Bowser_Sprite_NSMBW.png")
mario=load("images/Mario.png")
grass=load("images/ItemBlock.png")
luigi=load("images/Luigi.png")
run=1
pygame.display.set_caption("Super Mario Bros. Galaxy")
q=1
blit(titlescreen, [0,0])
blit(rosalina, [172, 357])
blit(bowser, [420, 300])
blit(mario, [50, 378])
blit(luigi, [100, 376])

for i in range(0, 640, grass.get_rect().width):
    blit(grass, [i, 429])

while run:
    flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=0
            q=1
        elif event.type==pygame.KEYDOWN and event.key==ord("x"):
            run=0
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            music.pause()
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_p:
            music.unpause()

if q:pygame.quit()

