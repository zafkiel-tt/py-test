import pygame,os
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
pygame.init()

#name
pygame.display.set_caption("THE DUCK")

#player img
duck_resolution= pygame.image.load(os.path.join("picture","duck.png"))
pygame.display.set_icon(duck_resolution)
duck=pygame.transform.scale(duck_resolution,(88,88))
duck_rect=duck.get_rect(center=(100,384))

#apple
icon=pygame.image.load(os.path.join("picture","apple.png"))
apple=pygame.transform.scale(icon,(88,88))
apple_rect=apple.get_rect(center=(100,384))

#floor
floor=pygame.image.load(os.path.join("picture","floor.png"))
floor_x_pos=0


#resolution
screen= pygame.display.set_mode((432,768))                
                                     
#FPS
clock=pygame.time.Clock()

#background()
bg=pygame.image.load(os.path.join('picture','bg.png'))
background = pygame.transform.scale(bg,(432,768))

#music
sfx=pygame.mixer.music.load('music/sfx.mp3')
pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=0 )

#object
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.exit()  
    screen.blit(background,(0,0))
    screen.blit(apple,apple_rect)
    screen.blit(duck,duck_rect)
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos<=-432:
        floor_x_pos=0
    pygame.display.update()
    clock.tick(120) 