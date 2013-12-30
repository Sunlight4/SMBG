import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        self.image = pygame.image.load(img)
        self.pos = pos
    def render(self,surf):
        surf.blit(self.img,self.pos)
    def update(self, room):pass
class Goomba(Object):
    def __init__(self, x, y):
        pos=[x,y]
        super(Goomba, self).__init__(pos, "images/Goomba.png")
    def update(self, room):
        pass # this is gonna get better

        

