import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        self.center = (400, 300)

        # загрузка руки
        path = os.path.join("images", "mickey_hand.png")
        if os.path.exists(path):
            self.hand = pygame.image.load(path)
        else:
            self.hand = pygame.Surface((100, 20))
            self.hand.fill((0, 0, 0))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            now = datetime.datetime.now()
            minutes = now.minute
            seconds = now.second

            minute_angle = -(minutes * 6)
            second_angle = -(seconds * 6)

            # правая рука (минуты)
            hand1 = pygame.transform.rotate(self.hand, minute_angle)
            rect1 = hand1.get_rect(center=(self.center[0] + 30, self.center[1]))
            self.screen.blit(hand1, rect1)

            # левая рука (секунды)
            hand2 = pygame.transform.rotate(self.hand, second_angle)
            rect2 = hand2.get_rect(center=(self.center[0] - 30, self.center[1]))
            self.screen.blit(hand2, rect2)

            pygame.display.flip()
            self.clock.tick(30)