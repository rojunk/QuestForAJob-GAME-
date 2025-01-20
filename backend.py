import pygame
from scenes import MenuScene


class SceneManager:
    def __init__(self):
        self.current_scene = MenuScene()

    def change_scene(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0),center=(100, 100), radius=30) #Test
        self.current_scene.draw(screen)
