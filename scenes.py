import pygame
import os

class MenuScene:
    def __init__(self):
        self.frames = []
        self.frame_index = 0
        self.frame_display_count = 0
        self.frame_delay = 2
        self.load_frames()

    def load_frames(self):
        for filename in sorted(os.listdir('media/menu')):
            if filename.endswith(".png"):
                self.frames.append(pygame.image.load(os.path.join('media/menu', filename)))

    def handle_event(self, event):
        pass

    def update(self):
        self.frame_display_count += 1
        if self.frame_display_count >= self.frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.frames)  # Loop back to the first frame
            self.frame_display_count = 0

    def draw(self, screen):
        if self.frames:
            background = self.frames[self.frame_index]
            scaled_background = pygame.transform.smoothscale(background, screen.get_size())
            screen.blit(scaled_background, (0, 0))
        pygame.draw.circle(screen, (255, 255, 0), center=(200, 200), radius=30)  # Test







class OptionsScene:
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 50), center=(200, 200), radius=30)  # Test