import pygame, easygui
pygame.init()
mixer = pygame.mixer
mixer.init()
music=mixer.music
music.load("music/Titles/Title.ogg")
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
starbunny=load("images/StarBunny.png")
topmaniac=load("images/Topmaniac.png")
fireflower=load("images/Fireflower.png")
firemario=load("images/Fire_Mario_Sprite.png")
powerstar=load("images/PowerStar.png")
kamella=load("images/Kamella.png")
kamek=load("images/KamekBroomstick.png")
peach=load("images/Princess_Peach_Model_NSMBW.png")
toad=load("images/ToadNSMBW.png")
goomboss=load("images/Goomboss.png")
images=[mario, luigi, rosalina, bowser, grass, starbunny, topmaniac, fireflower,
        firemario, powerstar, kamella, kamek, peach, toad, goomboss]
run=1
pygame.display.set_caption("Super Mario Bros. Galaxy")
q=1
blit(titlescreen, [0,0])
blit(rosalina, [172, 357])
blit(bowser, [420, 300])
blit(mario, [50, 378])
blit(luigi, [100, 376])
creditlist=["Super Mario Bros. Galaxy", "Created by Ian Huang and Ethan Saff",
            "Concept Development by creators and Isaac Saff", "Special Mention: David Saff",
            "Testing by all other people and Asher Saff.", "Credits to Nintendo",
            "Watch out for Bowser :-)",
            "Thanks everyone for playing!", "and have a nice day!"]
def credits_text():
    import random
    font=pygame.font.SysFont(None, 36)
    music.fadeout(1000)
    music.load("music/Titles/Credits.ogg")
    music.set_volume(1)
    music.play(-1)
    bg=load("bg/Aurora_Night_Sky.png")
    for i in creditlist:
        image=random.choice(images)
        text=font.render(i, False, [255, 0, 0])
        size=font.size(i)
        run2=True
        texty=500
        imgx=random.randrange(600)
        imgy=size[1]+200+random.randrange(100)
        while run2:
            fill([0,0,0])
            blit(bg, [0,0])
            for i in range(0, 640, grass.get_rect().width):
                blit(grass, [i, 429])
            
            texty-=3
            if random.random() < 0.005:
                image=random.choice(images)
                imgx=random.randrange(600)
                imgy=size[1]+200+random.randrange(100)
            blit(image, [imgx, imgy])
            blit(text, [320-size[0]//2, texty])
            flip()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        run2=False
                    elif event.key==pygame.K_q:
                        music.fadeout(1000)
                        music.load("music/Titles/Title.ogg")
                        music.set_volume(1)
                        music.play(-1)
                        return
            if texty+size[1] < 0:run2=False
        
                    
                    
            
                
        
        
    music.fadeout(1000)
    music.load("music/Titles/Title.ogg")
    music.set_volume(1)
    music.play(-1)

for i in range(0, 640, grass.get_rect().width):
    blit(grass, [i, 429])

while run:
    blit(titlescreen, [0,0])
    blit(titlescreen, [0,0])
    blit(rosalina, [172, 357])
    blit(bowser, [420, 300])
    blit(mario, [50, 378])
    blit(luigi, [100, 376])
    for i in range(0, 640, grass.get_rect().width):
        blit(grass, [i, 429])
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
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_c:
            credits_text()

if q:pygame.quit()

    
    

