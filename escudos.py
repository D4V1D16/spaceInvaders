import pygame 

class bloques (pygame.sprite.Sprite):
    def __init__(self,size,color,x,y):
        super().__init__()
        self.imagen = pygame.Surface((size,size))
        self.imagen.fill(color)
        self.rect = self.imagen.get_rect(topleft = (x,y))

shape =[
'  xxxxxxx',
' xxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxxxxxxxxxx',
'xxx     xxx',
'xx       xx']