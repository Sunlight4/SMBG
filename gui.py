import pygame

def button(text,size,posi,color,font=None,bg=[255,255,255],fsize=50,surf):
    f = pygame.font.Font(font,fsize)
    txt = f.render(text,color)
    surf.blit(txt,posi)
    pygame.display.flip()
    
    for event in pygame.event.get():
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] > posi[0]:
                if pos[0] < posi[1]:
                    if pos[1] > size[0]+posi[0]:
                        if pos[1] < size[1]+posi[1]:
                            return True
