"""
Sprite strip animator demo
 
Requires spritesheet.spritesheet and the Explode1.bmp through Explode5.bmp
found in the sprite pack at
http://lostgarden.com/2005/03/download-complete-set-of-sweet-8-bit.html
 
I had to make the following addition to method spritesheet.image_at in
order to provide the means to handle sprite strip cells with borders:
 
            elif type(colorkey) not in (pygame.Color,tuple,list):
                colorkey = image.get_at((colorkey,colorkey))
"""
import sys
import pygame
from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
import spritesheet
from sprite_strip_anim import SpriteStripAnim
 
surface = pygame.display.set_mode((200,200))
FPS = 6
frames = FPS / 6
strips = [
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('uppercut2.png', (0, 0, 36,85), 6, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('dodge_left1.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('dodge_right1.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 9, 6, True, frames),
    SpriteStripAnim('duck.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('hit.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('left1.png', (0, 0,36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('left2.png', (0, 0,36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('right1.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('right2.png', (0, 0, 36,85), 3, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('tired.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('defualt.png', (0, 0, 36,85), 2, 6, True, frames),
    SpriteStripAnim('win.png', (0, 0, 36,85), 2, 6, True, frames)
]
ringcolor = (102, 102, 153)
clock = pygame.time.Clock()
n = 0
strips[n].iter()
image = next(strips[n])
while True:
    for e in pygame.event.get():
        if e.type == KEYUP:
            if e.key == K_ESCAPE:
                sys.exit()
            elif e.key == K_RETURN:
                n += 1
                if n >= len(strips):
                    n = 0
                strips[n].iter()
    surface.fill(ringcolor)
    surface.blit(image, (100, 60))
    pygame.display.flip()
    image = next(strips[n])
    clock.tick(FPS)

