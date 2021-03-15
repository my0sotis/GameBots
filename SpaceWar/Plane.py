BACKGROUND = (200, 200, 200)
SCREEN_SIZE = (500, 600)


class Plane:
    def __init__(self, plane_image):
        self.plane_image = plane_image
        self.rect = plane_image.get_rect()

        self.width = self.rect[2]
        self.height = self.rect[3]
        self.x = SCREEN_SIZE[0] / 2 - self.width / 2
        self.y = SCREEN_SIZE[1] - self.height

        self.move_x = 0
        self.speed = 2

        self.alive = True

    def update(self):
        self.x += self.move_x * self.speed

    def draw(self, screen):
        screen.blit(self.plane_image, (self.x, self.y, self.width, self.height))

    def is_dead(self, enemes):
        if self.x < -self.width or self.x + self.width > SCREEN_SIZE[0] + self.width:
            return True

        for eneme in enemes:
            if self.collision(eneme):
                return True
        return False

    def collision(self, eneme):
        if not (self.x > eneme.x + eneme.width or self.x + self.width < eneme.x or self.y > eneme.y + eneme.height or self.y + self.height < eneme.y):
            return True
        else:
            return False

    def get_inputs_values(self, enemes, input_size=4):
        inputs = []

        for i in range(input_size):
            inputs.append(0.0)

        inputs[0] = (self.x * 1.0 / SCREEN_SIZE[0])
        index = 1
        for eneme in enemes:
            inputs[index] = eneme.x * 1.0 / SCREEN_SIZE[0]
            index += 1
            inputs[index] = eneme.y * 1.0 / SCREEN_SIZE[1]
            index += 1
        # if len(enemes) > 0:
        # distance = math.sqrt(math.pow(enemes[0].x + enemes[0].width/2 - self.x + self.width/2, 2) + math.pow(enemes[0].y + enemes[0].height/2 - self.y + self.height/2, 2));
        if len(enemes) > 0 and self.x < enemes[0].x:
            inputs[index] = -1.0
            index += 1
        else:
            inputs[index] = 1.0

        return inputs