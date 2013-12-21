import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        self.image = pygame.image.load(img)
        self.pos = pos
    def render(self,surf):
<<<<<<< HEAD
        surf.blit(self.img,self.pos)
=======
        surf.blit(self.image,self.pos)
    
>>>>>>> df0745527897a3018769313ce8b25e1e3c374dc9
