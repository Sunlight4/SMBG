import pygame
class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        self.image=pygame.image.load("images/"+image)
        self.pos=pos
        super(GameObject, self).__init__(self)
    def render(self, screen):
        screen.blit(self.image, self.pos)
    def get_rect(self):
        return self.image.get_rect(topleft=self.pos)
    def update(self, room):pass
class ArrowSign(GameObject):
    def __init__(self, *args):
        super(ArrowSign, self).__init__("ArrowSign.png", args)
class Ground(GameObject):pass
class Room(object):
    def __init__(self, bg, music, *objects):
        self.objects=objects
        self.bg=pygame.image.load("bg/"+bg)
        self.music=music
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/"+self.music)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)
    def __getitem__(self, index):
        return [obj for obj in self.objects if isinstance(obj, index)]
    def render(self, screen):
        screen.blit(self.bg, [0,0])
        for i in self.objects:
            i.render(screen)
    def update(self):
        for obj in objects:
            obj.update(self)
    def event(self, event):
        for i in [obj for obj in self.objects if hasattr(obj, "handle_event")]:
            obj.handle_event(event)
    
