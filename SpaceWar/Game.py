# coding:utf-8
# 创作者 马如云
import pygame
import sys
from pygame.locals import *
from Enemy import Enemy
from Plane import Plane
import neuro_evolution

BACKGROUND = (200, 200, 200)
SCREEN_SIZE = (500, 600)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Space War')
        self.background = pygame.image.load('background.png').convert()


        self.ai = neuro_evolution.NeuroEvolution()
        self.generation = 0

        self.max_enemes = 1
        # 加载飞机、敌机图片
        self.plane_image = pygame.image.load('plane.png').convert_alpha()
        self.enemy_image = pygame.image.load('enemy.png').convert_alpha()

    def start(self):
        self.score = 0
        self.planes = []
        self.enemes = []
        #self.myfont = pygame.font.Font(None, 30)  # test

        self.gen = self.ai.next_generation()
        for i in range(len(self.gen)):
            plane = Plane(self.plane_image)
            self.planes.append(plane)

        self.generation += 1
        self.alives = len(self.planes)

    def update(self, screen):
        for i in range(len(self.planes)):
            if self.planes[i].alive:
                inputs = self.planes[i].get_inputs_values(self.enemes)
                res = self.gen[i].feed_forward(inputs)
                if res[0] < 0.45:
                    self.planes[i].move_x = -1
                elif res[0] > 0.55:
                    self.planes[i].move_x = 1

                self.planes[i].update()
                self.planes[i].draw(screen)

                if self.planes[i].is_dead(self.enemes) == True:
                    self.planes[i].alive = False
                    self.alives -= 1
                    self.ai.network_score(self.score, self.gen[i])
                    if self.is_ai_all_dead():
                        self.start()

        self.gen_enemes()

        for i in range(len(self.enemes)):
            self.enemes[i].update()
            self.enemes[i].draw(screen)
            if self.enemes[i].is_out():
                del self.enemes[i]
                break

        self.score += 1
        end = '\r'
        print("alive:{}, generation:{}, score:{}".format(self.alives, self.generation, self.score), end)

    def run(self, FPS=1000):
        #max_score = 0
        while True:
            #if max_score < self.score:
             #   max_score = self.score
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.background, (0, 0))

            self.update(self.screen)

            # self.screen.blit(self.myfont.render('generous:{}'.format(self.generation), True, (255, 255, 255)), (10, 10))
            # self.screen.blit(self.myfont.render('max_score:{}'.format(max_score), True, (255, 255, 255)), (175, 10))
            # self.screen.blit(self.myfont.render('score:{}'.format(self.score), True, (255, 255, 255)), (375, 10))

            pygame.display.update()
            self.clock.tick(FPS)

    def gen_enemes(self):
        if len(self.enemes) < self.max_enemes:
            enemy = Enemy(self.enemy_image)
            self.enemes.append(enemy)

    def is_ai_all_dead(self):
        for plane in self.planes:
            if plane.alive:
                return False
        return True


game = Game()
game.start()
game.run()
