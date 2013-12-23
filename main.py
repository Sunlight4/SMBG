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
thank_you=mixer.Sound("sounds/thank_you.wav")
power_star=mixer.Sound("sounds/powerstar_mario.wav")
images=[mario, luigi, rosalina, bowser, starbunny, topmaniac, fireflower,
        firemario, powerstar, kamella, kamek, peach, toad, goomboss]
musicstotest=[("Peach Castle", "music/HomeBase/PeachCastle.ogg"),
              ("World 1:Here We Go!", "music/HomeBase/GrassMap.ogg"), ("Goomba Garden", "music/Areas/BiancoHills.ogg"),
              ("Mystery Box", "music/Areas/AthleticMystery.ogg"),
              ("Goomboss in The Garden", "music/Bosses/MiniBossSMGRemix.ogg"), ("Planet Plains", "music/Areas/GoodEggGalaxy.ogg"),
              ("Dino Piranha", "music/Bosses/MiniBossSMG.ogg"), ("Bobomb Battlefield", "music/Areas/BobombBattlefield.ogg"),
              ("King Bob-omb on the Mountain", "music/Bosses/BossClassicSMG.ogg"), ("Queen Bee's Honeyhive", "music/Areas/Honeyhive.ogg"),
              ("Big Bad Bugaboom", "music/Areas/BigBadBugaboom.ogg"), ("Bowser's Airship","music/Areas/AirshipBGM.ogg"),
              ("Bowser #1", "music/Bosses/Bowser/BowserBattleNSMBW.ogg"), ("To Starship Mario", "music/HomeBase/StarshipMario1.ogg"),
              ("World 2:The Great Space Journey Begins", "music/HomeBase/World2.ogg"), ("Sky Station", "music/Areas/SkyStation.ogg"),
              ("Peewee Piranha", "music/Bosses/BossTheme1SMG2.ogg"), ("Space Junk Road", "music/Areas/DeepSpace.ogg"),
              ("Cosmic Mario Cataclysm", "music/Bosses/BossCosmic.ogg"), ("Bullet Barrage Galaxy", "music/Areas/SpaceStation.ogg"),
              ("Megaleg's Moon", "music/Bosses/BossRobot.ogg"), ("Freezeflame:Ice Maze", "music/Areas/IceCave.ogg"),
              ("King Brrr's Frozen Iceberg", "music/Bosses/BossIce.ogg"), ("Freezeflame:Lava Mountain", "music/Areas/BlisteringCore.ogg"),
              ("Bowser Jr.'s Heavy-Metal Reactor", "music/Bosses/BossHeavyMetal.ogg"),
              ("Topmaniac and the Topman Tribe", "music/Bosses/BossHeavyMetalSMG2.ogg"), ("World 3:Return of the Mushroom Kingdom",
                                                                                          "music/HomeBase/SnowMap.ogg"),
              ("Layer-Cake Desert", "music/Areas/DesertBGM.ogg"), ("Hazy Maze Cave", "music/Areas/UndergroundSM64.ogg"),
              ("Boo's Mansion", "music/Areas/GhostHouseNSMBW.ogg"), ("King Boo's Haunt", "music/Bosses/BossClassicSMS.ogg"),
              ("Bully Arena", "music/Areas/AthleticHeavyMetal.ogg"), ("Big Bully's Tower", "music/Bosses/BossClassicSM64.ogg"),
              ("Bowser Jr.'s Dire Dire Docks", "music/Areas/BuoyBaseGalaxy.ogg"), ("Gooper Blooper", "music/Bosses/BossTheme2SMG2.ogg"),
              ("World 4:Elemental Roulette", "music/HomeBase/LubbasStory.ogg"), ("Gusty Garden Winds", "music/Areas/GustyGardenGalaxy.ogg"),
              ("Yoshi Cape Galaxy", "music/Areas/TropicalParadise.ogg"), ("Sea Ring Galaxy", "music/Areas/BeachGrass.ogg"),
              ("Going After Guppy", "music/Areas/AquaticRace.ogg"), ("Cyclone Stone Galaxy", "music/Areas/AthleticCosmos.ogg")]
run=1

pygame.display.set_caption("Super Mario Bros. Galaxy")
q=0
blit(titlescreen, [0,0])
blit(rosalina, [172, 357])
blit(bowser, [420, 300])
blit(mario, [50, 378])
blit(luigi, [100, 376])
creditlist=["Super Mario Bros. Galaxy", "Created by Ian Huang and Ethan Saff",
            "Concept Development by creators and Isaac Saff", "Special Mention: David Saff",
            "Testing by all other people and Asher Saff.", "Credits to Nintendo",
            "Music and sprites by mariomayhem.com","nindendo3dscomunity.com","fantendo.com",
            "wikipedia.com","Please add more, Ethan! :D",
            "Also, watch out for Bowser :D",
            "Credits to http://www.spriters-resource.com/ for some sprites",
            "Thanks for playing!"]

def starshipmario():
    run = 1

    font = pygame.font.Font("Delfino.ttf",30)
    welcome = font.render("Welcome to Starship Mario!",0,[0,0,0])
    screen.blit(welcome,[50,50])

    music.load("music/Areas/home.mp3")
    music.set_volume(1)
    music.play(-1)
    bg=load("bg/Aurora_Night_Sky.png")
    blit(bg, [0,0])
    screen.blit(welcome,[50,50])
    pygame.display.flip()            
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'q'
        
def music_test():
    font=pygame.font.SysFont(None, 36)
    bg=load("bg/Aurora_Night_Sky.png")
    music.fadeout(1000)
    i=0
    while i<len(musicstotest):
        k, v=musicstotest[i]
        size=font.size(k)
        music.stop()
        text=font.render(k, False, [255,0,0])
        music.load(v)
        music.set_volume(1)
        music.play(-1)
        run2=True
        while run2:
            fill([0,0,0])
            blit(bg, [0,0])
            blit(text, [320-size[0]//2, 200])
            flip()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:run2=False
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:run2=False; i-=2
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_r:music.rewind()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    music.pause()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                    music.unpause()
                elif event.type==pygame.KEYDOWN and event.key==pygame.K_q:
                        music.fadeout(1000)
                        music.load("music/Titles/Title.ogg")
                        music.set_volume(1)
                        music.play(-1)
                        return
        i+=1

    music.fadeout(1000)
    music.load("music/Titles/Title.ogg")
    music.set_volume(1)
    music.play(-1)
        
                
                    
    
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
        imgy=429-image.get_rect().height
        while run2:
            fill([0,0,0])
            blit(bg, [0,0])
            for i in range(0, 640, grass.get_rect().width):
                blit(grass, [i, 429])
            
            texty-=3
            if random.random() < 0.005:
                image=random.choice(images)
                imgx=random.randrange(600)
                imgy=429-image.get_rect().height
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
    power_star.play()
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
        elif event.type==pygame.KEYDOWN and event.key==pygame.K_m:
            music_test()

if q:
    pygame.quit()
else:
    screen.fill([255,255,255])

    if starshipmario() == 'q':
        pygame.quit()

    
    

