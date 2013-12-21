import pygame

class Room:
    def __init__(self,objs,bg): # objs includes tiles
        self.objs = objs
        self.bg = bg
    def update(self,surf):
        for obj in objs:
            obj.render(surf)
        
