import pygame

pygame.init()

window = pygame.display.set_mode((1600,900), pygame.RESIZABLE)
pygame.display.set_caption('HelloWorld')

screen = pygame.Surface((1920,1080))

running = True
is_fullscreen = False

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
            else:
                window = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)


    scaled_screen = pygame.transform.smoothscale(screen, screen.get_size())


    window.fill((0,0,25))
    screen.fill((255,0,0))
    window.blit(screen, (0,0))
    pygame.display.flip()
