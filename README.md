
Spritesheet

the pygame Spritesheet animation demo working on python 3.4


http://www.pygame.org/wiki/Spritesheet

Just saving the python 3.4 working verision for reference...

'''
import spritesheet
...
ss = spritesheet.spritesheet('somespritesheet.png')

Sprite is 16x16 pixels at location 0,0 in the file...

image = ss.image_at((0, 0, 16, 16))
images = []


Load two images into an array, their transparent bit is (255, 255, 255)

images = ss.images_at((0, 0, 16, 16),(17, 0, 16,16), colorkey=(255, 255, 255))


...

Requires spritesheet.spritesheet and the Explode1.bmp through Explode5.bmp
found in the sprite pack at


http://lostgarden.com/2005/03/download-complete-set-of-sweet-8-bit.html

'''
