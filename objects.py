import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,pos,img):
        self.image = pygame.image.load(img)
        self.pos = pos
    def render(self,surf):
        surf.blit(self.image,self.pos)
    
