import pygame, importlib, inspect
import scenes



class SceneManager:
    def __init__(self):
        self.scene_map = self.load_scenes()
        self.current_scene = self.scene_map['MenuScene']()

    def load_scenes(self):
        scene_map = {}
        for name, obj in inspect.getmembers(scenes, inspect.isclass):
            scene_map[name] = obj
        return scene_map

    def change_scene(self, scene_name):
        self.current_scene = self.scene_map[scene_name]()
        pass

    def handle_event(self, event):
        self.current_scene.handle_event(event)

    def update(self):
        self.current_scene.update()

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0),center=(100, 100), radius=30) #Test
        self.current_scene.draw(screen)
