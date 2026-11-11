
import pygame
pygame.init()
pygame.mixer.init()#allow music
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Maize Game")
clock=pygame.time.Clock()
#BG muisic
pygame.mixer.music.load("lnplusmusic-background-music-628850.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)#loop the music
#player
player=pygame.image.load("image.png").convert_alpha()
player=pygame.transform.scale(player,(30,30))
player_rect=player.get_rect(topleft=(40,40))
#maze walls
walls=[
    pygame.Rect(0,0,800,20),
    pygame.Rect(0,0,20,600),
    pygame.Rect(0,580,800,20),
    pygame.Rect(780,0,20,600),
    pygame.Rect(100,100,450,20),
    pygame.Rect(100,100,20,300),
    pygame.Rect(250,480,450,20),
    pygame.Rect(680,180,20,320),
    pygame.Rect(200,200,280,20),
    pygame.Rect(200,200,20,120),
    pygame.Rect(320,380,280,20),
    pygame.Rect(580,280,20,120),
    pygame.Rect(300,300,200,20)
]
#goal
goal=pygame.Rect(700,500,50,50)
font=pygame.font.SysFont("Sans-Serif", 48)
running=True
won=False
while running:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not won:
        old_x=player_rect.x
        old_y=player_rect.y
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x-=3
        if keys[pygame.K_RIGHT]:
            player_rect.x+=3
        if keys[pygame.K_UP]:
            player_rect.y-=3
        if keys[pygame.K_DOWN]:
            player_rect.y+=3
        #wall collision
        for wall in walls:
            if player_rect.colliderect(wall):
                player_rect.x=old_x
                player_rect.y=old_y
        #draw the walls
        for wall in walls:
            pygame.draw.rect(screen,"black",wall)
        #goal
        pygame.draw.rect(screen,"green",goal)
        #player
        screen.blit(player,player_rect)
        #check for win
        if player_rect.colliderect(goal):
            won=True
            pygame.mixer.music.stop()#stop the music
    else:
        text=font.render("You Win!",True,"blue")
        text_rect=text.get_rect(center=(400,300))
        screen.blit(text,text_rect)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
