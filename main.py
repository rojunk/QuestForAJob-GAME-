import pygame
from backend import SceneManager

pygame.init()

window = pygame.display.set_mode((1600,900), pygame.RESIZABLE)
pygame.display.set_caption('HelloWorld')
screen = pygame.Surface((1920,1080))

clock = pygame.time.Clock()
scene_manager = SceneManager()

running = True
global is_fullscreen
is_fullscreen = False


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.VIDEORESIZE:
                desired_ratio = 16 / 9
                new_w, new_h = event.w, event.h
                actual_ratio = new_w / new_h if new_h != 0 else desired_ratio
                if actual_ratio > desired_ratio:
                    new_w = int(new_h * desired_ratio)
                else:
                    new_h = int(new_w / desired_ratio)
                window = pygame.display.set_mode((new_w, new_h), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN and ((pygame.key.get_mods() & pygame.KMOD_ALT) and event.key == pygame.K_RETURN):
            is_fullscreen = not is_fullscreen
            if is_fullscreen:
                window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
            else:
                window = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
        scene_manager.handle_event(event)

    window.fill((0,0,25))

    scene_manager.update()
    scene_manager.draw(screen)

    scaled_screen = pygame.transform.smoothscale(screen, window.get_size())


    window.blit(scaled_screen, (0,0))
    pygame.display.flip()

    clock.tick(60)

