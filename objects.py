import pygame
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        self.img=pygame.image.load("images/"+image)
        self.pos=pos
        super(GameObject, self).__init__(self)
        self.rect=self.img.get_rect(topleft=pos)
    def render(self, screen):
        screen.blit(self.img, self.pos)
class ArrowSign(GameObject):
    def __init__(self, *args):
        super(ArrowSign, self).__init__("ArrowSign.png", args)
