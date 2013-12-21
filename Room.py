import pygame

class Room:
    def __init__(self,objs,bg,bgmusic): # objs includes tiles
        self.objs = objs
        self.bg = bg
        self.bgmusic = bgmusic
    def update(self,surf):
        for obj in objs:
            obj.render(surf)
    def init(self,surf): # init for initalize. func initalizes the room
        for obj in objs:
            obj.render(surf)

        pygame.mixer.music.load(bgmusic)
        music.set_volume(1)
        pygame.mixer.music.play(-1)
            
