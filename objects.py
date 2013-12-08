import pygame
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        self.img=pygame.image.load("images/"+image)
        self.pos=pos
        super(GameObject, self).__init__(self)
        self.rect=self.img.get_rect(topleft=pos)

        
