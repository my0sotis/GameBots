import random

SCREEN_SIZE = (500, 600)


class Enemy:
    def __init__(self, enemy_image):
        self.enemy_image = enemy_image
        self.rect = enemy_image.get_rect()

        self.width = self.rect[2]
        self.height = self.rect[3]
        self.x = random.choice(range(0, int(SCREEN_SIZE[0] - self.width / 2), 71))
        self.y = 0

    def update(self):
        self.y += 6

    def draw(self, screen):
        screen.blit(self.enemy_image, (self.x, self.y, self.width, self.height))

    def is_out(self):
        return True if self.y >= SCREEN_SIZE[1] else False