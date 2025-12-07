import pygame
import threading
import time

SCREEN_SIZE = (300, 300)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 191, 255)
RED = (255, 50, 50)

class RobotFace:
    def __init__(self):
        pygame.init()
        self.screen = None
        self.running = False
        self.current_emotion = "正常"

        self.eye_color = BLUE
        self.eye_size = 30
    
    def start(self):
        """启动窗口循环"""
        self.running = True
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Robo Face")

        while self.running:
            self.draw()
            self.update_state()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.time.Clock().tick(30)
        pygame.quit()

    def update_state(self):
        if self.current_emotion == "开心":
            self.eye_color = (255, 200, 0)
            self.eye_size = 40
        elif self.current_emotion == "生气":
            self.eye_color = RED
            self.eye_size = 25
        elif self.current_emotion == "难过":
            self.eye_color = (0, 0, 150)
            self.eye_size = 20
        else:
            self.eye_color = BLUE
            self.eye_size = 30

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.circle(self.screen, self.eye_color, (100, 150), self.eye_size)
        pygame.draw.circle(self.screen, self.eye_color, (200, 150), self.eye_size)
        pygame.display.flip()

    def set_emotion(self, emotion):
        print(f"emotion changing: {emotion}")
        self.current_emotion = emotion

face_app = RobotFace()

if __name__ == "__main__":
    face_app.start()

            