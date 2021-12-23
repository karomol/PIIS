from collections import defaultdict
import csv

import pygame
import random
import pygame.freetype
import sys
import os
import BFS_alg
import DFS_alg
import A_star_alg
import const
import MinimaxExpectimax


FILENAME = "statistic.csv"





depth = 10



def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

def main():
    WIDTH = 800
    HEIGHT = 650
    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Let's battle!")
    clock = pygame.time.Clock()

    destination_path = 'sprite_images/diamond.tga'
    cross_path = 'sprite_images/krest.jpg'
    background_path = 'sprite_images/ground02.bmp'
    player_img1_path = 'sprite_images/pla1.bmp'
    player_img2_path = 'sprite_images/pla2.bmp'
    player_img3_path = 'sprite_images/pla3.bmp'
    player_img4_path = 'sprite_images/pla4.bmp'
    obstacle_img1_path = 'sprite_images/block_02.bmp'
    obstacle_img2_path = 'sprite_images/block_08.bmp'
    bullet1_img_path = 'sprite_images/bullet1.png'
    bullet2_img_path = 'sprite_images/bullet2.png'
    bullet3_img_path = 'sprite_images/bullet3.png'
    bullet4_img_path = 'sprite_images/bullet4.png'
    mob_3_img1_path = 'sprite_images/s1.bmp'
    mob_3_img2_path = 'sprite_images/s2.bmp'
    mob_3_img3_path = 'sprite_images/s3.bmp'
    mob_3_img4_path = 'sprite_images/s4.bmp'
    mob_2_img1_path = 'sprite_images/t1.bmp'
    mob_2_img2_path = 'sprite_images/t2.bmp'
    mob_2_img3_path = 'sprite_images/t3.bmp'
    mob_2_img4_path = 'sprite_images/t4.bmp'
    mob_img1_path = 'sprite_images/v1.bmp'
    mob_img2_path = 'sprite_images/v2.bmp'
    mob_img3_path = 'sprite_images/v3.bmp'
    mob_img4_path = 'sprite_images/v4.bmp'
    back_img_path = 'sprite_images/i_background.jpg'
    panel_path = 'sprite_images/panel.bmp'
    player_img_mini_path = 'sprite_images/pla1_mini.bmp'
    img_exp0_path = 'sprite_images/regularExplosion00.png'
    img_exp1_path = 'sprite_images/regularExplosion01.png'
    img_exp2_path = 'sprite_images/regularExplosion02.png'
    img_exp3_path = 'sprite_images/regularExplosion03.png'
    img_exp4_path = 'sprite_images/regularExplosion04.png'
    img_exp5_path = 'sprite_images/regularExplosion05.png'
    img_exp6_path = 'sprite_images/regularExplosion06.png'
    img_exp7_path = 'sprite_images/regularExplosion07.png'
    img_exp8_path = 'sprite_images/regularExplosion08.png'
    shoot_sound_path = 'sounds/shoot.wav'
    enemy_shoot_sound_path = 'sounds/enemy_shoot.wav'
    enemy_hit_path = 'sounds/enemy_hit.wav'
    god_mode_on_path = 'sounds/Powerup.wav'
    god_mode_off_path = 'sounds/Powerup1.wav'
    bullets_hit_path = 'sounds/Hit_Hurt.wav'
    player_hit_path = 'sounds/player_kill.wav'



    # destination_path = resource_path(os.path.join('sprite_images', 'diamond.tga'))
    # cross_path = resource_path(os.path.join('sprite_images', 'krest.jpg'))
    # background_path = resource_path(os.path.join('sprite_images', 'ground02.bmp'))
    # player_img1_path = resource_path(os.path.join('sprite_images', 'pla1.bmp'))
    # player_img2_path = resource_path(os.path.join('sprite_images', 'pla2.bmp'))
    # player_img3_path = resource_path(os.path.join('sprite_images', 'pla3.bmp'))
    # player_img4_path = resource_path(os.path.join('sprite_images', 'pla4.bmp'))
    # obstacle_img1_path = resource_path(os.path.join('sprite_images', 'block_02.bmp'))
    # obstacle_img2_path = resource_path(os.path.join('sprite_images', 'block_08.bmp'))
    # bullet1_img_path = resource_path(os.path.join('sprite_images', 'bullet1.png'))
    # bullet2_img_path = resource_path(os.path.join('sprite_images', 'bullet2.png'))
    # bullet3_img_path = resource_path(os.path.join('sprite_images', 'bullet3.png'))
    # bullet4_img_path = resource_path(os.path.join('sprite_images', 'bullet4.png'))
    # mob_3_img1_path = resource_path(os.path.join('sprite_images', 's1.bmp'))
    # mob_3_img2_path = resource_path(os.path.join('sprite_images', 's2.bmp'))
    # mob_3_img3_path = resource_path(os.path.join('sprite_images', 's3.bmp'))
    # mob_3_img4_path = resource_path(os.path.join('sprite_images', 's4.bmp'))
    # mob_2_img1_path = resource_path(os.path.join('sprite_images', 't1.bmp'))
    # mob_2_img2_path = resource_path(os.path.join('sprite_images', 't2.bmp'))
    # mob_2_img3_path = resource_path(os.path.join('sprite_images', 't3.bmp'))
    # mob_2_img4_path = resource_path(os.path.join('sprite_images', 't4.bmp'))
    # mob_img1_path = resource_path(os.path.join('sprite_images', 'v1.bmp'))
    # mob_img2_path = resource_path(os.path.join('sprite_images', 'v2.bmp'))
    # mob_img3_path = resource_path(os.path.join('sprite_images', 'v3.bmp'))
    # mob_img4_path = resource_path(os.path.join('sprite_images', 'v4.bmp'))
    # back_img_path = resource_path(os.path.join('sprite_images', 'i_background.jpg'))
    # panel_path = resource_path(os.path.join('sprite_images', 'panel.bmp'))
    # player_img_mini_path = resource_path(os.path.join('sprite_images', 'pla1_mini.bmp'))
    # img_exp0_path = resource_path(os.path.join('sprite_images', 'regularExplosion00.png'))
    # img_exp1_path = resource_path(os.path.join('sprite_images', 'regularExplosion01.png'))
    # img_exp2_path = resource_path(os.path.join('sprite_images', 'regularExplosion02.png'))
    # img_exp3_path = resource_path(os.path.join('sprite_images', 'regularExplosion03.png'))
    # img_exp4_path = resource_path(os.path.join('sprite_images', 'regularExplosion04.png'))
    # img_exp5_path = resource_path(os.path.join('sprite_images', 'regularExplosion05.png'))
    # img_exp6_path = resource_path(os.path.join('sprite_images', 'regularExplosion06.png'))
    # img_exp7_path = resource_path(os.path.join('sprite_images', 'regularExplosion07.png'))
    # img_exp8_path = resource_path(os.path.join('sprite_images', 'regularExplosion08.png'))
    # shoot_sound_path = resource_path(os.path.join('sounds', 'shoot.wav'))
    # enemy_shoot_sound_path = resource_path(os.path.join('sounds', 'enemy_shoot.wav'))
    # enemy_hit_path = resource_path(os.path.join('sounds', 'enemy_hit.wav'))
    # god_mode_on_path = resource_path(os.path.join('sounds', 'Powerup.wav'))
    # god_mode_off_path = resource_path(os.path.join('sounds', 'Powerup1.wav'))
    # bullets_hit_path = resource_path(os.path.join('sounds', 'Hit_Hurt.wav'))
    # player_hit_path = resource_path(os.path.join('sounds', 'player_kill.wav'))


    destination_img = pygame.image.load(destination_path).convert()
    destination_img = pygame.transform.scale(destination_img, (50, 50))


    cross_img = pygame.image.load(cross_path).convert()
    cross_img = pygame.transform.scale(cross_img, (50, 50))
    cross_img.set_colorkey(WHITE)


    background = pygame.image.load(background_path).convert()
    background = pygame.transform.scale(background, (800, 700))
    background_rect = background.get_rect()


    player_img1 = pygame.image.load(player_img1_path).convert()


    player_img2 = pygame.image.load(player_img2_path).convert()

    player_img3 = pygame.image.load(player_img3_path).convert()
    player_img4 = pygame.image.load(player_img4_path).convert()

    obstacle_img1 = pygame.image.load(obstacle_img1_path).convert()
    obstacle_img2 = pygame.image.load(obstacle_img2_path).convert()
    bullet1_img = pygame.image.load(bullet1_img_path).convert()
    bullet2_img = pygame.image.load(bullet2_img_path).convert()
    bullet3_img = pygame.image.load(bullet3_img_path).convert()
    bullet4_img = pygame.image.load(bullet4_img_path).convert()

    mob_3_img1 = pygame.image.load(mob_3_img1_path).convert()
    mob_3_img2 = pygame.image.load(mob_3_img2_path).convert()
    mob_3_img3 = pygame.image.load(mob_3_img3_path).convert()
    mob_3_img4 = pygame.image.load(mob_3_img4_path).convert()

    mob_2_img1 = pygame.image.load(mob_2_img1_path).convert()
    mob_2_img2 = pygame.image.load(mob_2_img2_path).convert()
    mob_2_img3 = pygame.image.load(mob_2_img3_path).convert()
    mob_2_img4 = pygame.image.load(mob_2_img4_path).convert()

    mob_img1 = pygame.image.load(mob_img1_path).convert()
    mob_img2 = pygame.image.load(mob_img2_path).convert()
    mob_img3 = pygame.image.load(mob_img3_path).convert()
    mob_img4 = pygame.image.load(mob_img4_path).convert()

    back_img = pygame.image.load(back_img_path).convert()
    back_img = pygame.transform.scale(back_img, (800, 700))
    back_img_rect = back_img.get_rect()
    panel = pygame.image.load(panel_path).convert()
    panel = pygame.transform.scale(panel, (WIDTH, 50))
    panel_rect = panel.get_rect()
    panel_rect.x = 0
    panel_rect.y = 0
    player_img_mini = pygame.image.load(player_img_mini_path).convert()
    player_img_mini = pygame.transform.scale(player_img_mini, (25, 25))
    player_img_mini.set_colorkey(WHITE)

    img_exp0 = pygame.image.load(img_exp0_path).convert()
    img_exp1 = pygame.image.load(img_exp1_path).convert()
    img_exp2 = pygame.image.load(img_exp2_path).convert()
    img_exp3 = pygame.image.load(img_exp3_path).convert()
    img_exp4 = pygame.image.load(img_exp4_path).convert()
    img_exp5 = pygame.image.load(img_exp5_path).convert()
    img_exp6 = pygame.image.load(img_exp6_path).convert()
    img_exp7 = pygame.image.load(img_exp7_path).convert()
    img_exp8 = pygame.image.load(img_exp8_path).convert()

    shoot_sound = pygame.mixer.Sound(shoot_sound_path)
    enemy_shoot_sound = pygame.mixer.Sound(enemy_shoot_sound_path)
    enemy_hit = pygame.mixer.Sound(enemy_hit_path)
    god_mode_on = pygame.mixer.Sound(god_mode_on_path)
    god_mode_off = pygame.mixer.Sound(god_mode_off_path)
    bullets_hit = pygame.mixer.Sound(bullets_hit_path)
    player_hit = pygame.mixer.Sound(player_hit_path)

    explosion_anim = []
    explosion_anim.append(img_exp0)
    explosion_anim.append(img_exp1)
    explosion_anim.append(img_exp2)
    explosion_anim.append(img_exp3)
    explosion_anim.append(img_exp4)
    explosion_anim.append(img_exp5)
    explosion_anim.append(img_exp6)
    explosion_anim.append(img_exp7)
    explosion_anim.append(img_exp8)

    for i in range(9):
        explosion_anim[i] = pygame.transform.scale(explosion_anim[i], (32, 32))
        explosion_anim[i].set_colorkey(BLACK)

    minimax = False
    random_map = False
    respawn_number = 3
    chaser_mob = 2
    random_mob = 3
    solid_obstacles = 62
    destructible_obstacles = 0
    player_lives = 5
    player_coordinates = (0, 12)
    destination = 10

    free_location = list()
    free_location.append(player_coordinates)
    free_location.append((random.randrange(0, 10), 1))
    free_location.append((15, random.randrange(1, 9)))
    free_location.append((random.randrange(5, 10), random.randrange(5, 13)))
    free_location.append((random.randrange(12, 16), random.randrange(11, 13)))


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img1, (50, 50))
            self.rect = self.image.get_rect()
            self.image.set_colorkey(WHITE)
            self.rect.left = player_coordinates.__getitem__(0) * 50
            self.rect.top = player_coordinates.__getitem__(1) * 50
            self.speedx = 0
            self.speedy = 0
            self.direction = ''
            self.cooldown = 1300
            self.alg = False
            self.shottime = -self.cooldown
            self.bulletspeed = 5
            self.speed = 1
            self.points = 0
            self.lives = player_lives
            self.god_mode = False
            self.is_detected = False
            self.safe_location = player_coordinates
            self.autopilot_on = False
            self.autopilot_pause = 500
            self.autopilot_time = pygame.time.get_ticks()-self.autopilot_pause
            self.autopilot_path = list()
            self.vertex_list = list()
            if not random_map:
                self.vertex_list = create_vertex()
            self.destination_on = True
            self.destination_coordinates = (0, 0)
            self.destination_points = 0
            self.target_index = 0







        def update(self):

            if self.alg:
                if minimax:
                    move = MinimaxExpectimax.minimax(self, depth, create_vertex()[self.rect.x, self.rect.y], create_graph())
                else:
                    move = MinimaxExpectimax.expectimax(self, depth, create_vertex()[self.rect.x, self.rect.y], create_graph())



            self.speedx = 0
            self.speedy = 0

            def detected():
                self.safe_location = (-1, -1)
                self.is_detected = True

            if self.direction == 'left':
                self.image = pygame.transform.scale(player_img2, (50, 50))
                self.image.set_colorkey(WHITE)
            if self.direction == 'right':
                self.image = pygame.transform.scale(player_img3, (50, 50))
                self.image.set_colorkey(WHITE)
            if self.direction == 'up':
                self.image = pygame.transform.scale(player_img1, (50, 50))
                self.image.set_colorkey(WHITE)
            if self.direction == 'down':
                self.image = pygame.transform.scale(player_img4, (50, 50))
                self.image.set_colorkey(WHITE)

            if self.destination_on:
                if mobs.sprites().__len__() != 0:
                    location_list = []

                    for obj in mobs.sprites():
                        x = const.vertex_list[(obj.rect.centerx // 50, obj.rect.centery // 50)]
                        y = const.vertex_list[(self.rect.centerx // 50, self.rect.centery // 50)]
                        location_list.append(A_star_alg.astar(create_graph(), x, y).__len__())

                    self.target_index = location_list.index(min(location_list))
                    x = mobs.sprites()[self.target_index].rect.centerx
                    y = mobs.sprites()[self.target_index].rect.centery
                    if not autopilot(player, x, y):
                        self.destination_coordinates = (0, 0)
                        self.destination_on = False
                    else:
                        detected()
                else:
                        self.destination_on = False
                        alg = ''
                        if minimax:
                            alg = 'minimax'
                        else:
                            alg = 'expectimax'
                        with open(r'statistic.csv', 'a', newline='') as csvfile:
                            columns = ["win_or_lose", "time", "score", "alg"]
                            writer = csv.DictWriter(csvfile, fieldnames=columns)
                            result = {"win_or_lose": 1, "time": pygame.time.get_ticks(), "score": player.points, "alg": alg}
                            writer.writerow(result)


            # if self.destination_on:
            #
            #     print(destinations)
            #     # temp = 0
            #     # for item in mobs.sprites():
            #     #     if autopilot(player, destinations):
            #     #         detected()
            #     #         temp += 1
            #     #         break
            #     # if temp == 0:
            #     #     self.autopilot_on = False
            #     #     player.lives = player_lives

            if not self.autopilot_on and not self.destination_on:

                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    detected()
                    self.speedx = -self.speed
                    self.direction = 'left'
                elif keystate[pygame.K_RIGHT]:
                    detected()
                    self.speedx = self.speed
                    self.direction = 'right'
                elif keystate[pygame.K_UP]:
                    detected()
                    self.speedy = -self.speed
                    self.direction = 'up'
                elif keystate[pygame.K_DOWN]:
                    detected()
                    self.speedy = self.speed
                    self.direction = 'down'

                self.rect.x += self.speedx
                self.rect.y += self.speedy

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.top < 50:
                self.rect.top = 50
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

        def shoot(self):
            if pygame.time.get_ticks() >= self.shottime + self.cooldown:
                self.shottime = pygame.time.get_ticks()
                bullet = Bullet(self.rect.top, self.rect.bottom, self.rect.centerx, self.rect.centery,
                                self.rect.right, self.rect.left, self.direction, self.bulletspeed)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()

    class Mob(pygame.sprite.Sprite):
        def __init__(self, x1, y1, mob_type):
            pygame.sprite.Sprite.__init__(self)
            if mob_type == 0:
                self.image = pygame.transform.scale(mob_img3, (50, 50))
            if mob_type == 1:
                self.image = pygame.transform.scale(mob_2_img3, (50, 50))
            if mob_type == 2:
                self.image = pygame.transform.scale(mob_3_img3, (50, 50))
            self.rect = self.image.get_rect()
            self.image.set_colorkey(WHITE)
            self.rect.left = x1
            self.rect.top = y1
            self.speedy = 0
            self.speedx = 0
            self.cooldown = 1500
            self.shottime = -self.cooldown
            self.crashtime = random.randrange(300, 1000, 1)
            self.crashtime_step = random.randrange(300, 1000, 1)
            self.bulletspeed = 3
            self.speed = 1
            self.direction = ''
            self.step = 50
            self.locationx = x1
            self.locationy = y1 - self.step
            self.playerdirection = ' '
            self.autopilot_pause = random.randrange(800, 1000, 10)
            self.autopilot_time = pygame.time.get_ticks()-self.autopilot_pause
            self.autopilot_path = list()
            self.vertex_list = list()
            self.autopilot_on = True
            self.type = mob_type
            if self.type == 2:
                self.is_chaser = True
            else:
                self.is_chaser = False


        def update(self):

            def player_shoot(direction):
                if direction == 'up' and player.direction == 'down':
                    player.shoot()
                if direction == 'down' and player.direction == 'up':
                    player.shoot()
                if direction == 'left' and player.direction == 'right':
                    player.shoot()
                if direction == 'right' and player.direction == 'left':
                    player.shoot()

            def change_chaser():
                if self.type == 1:
                    self.is_chaser = True

            def sprite_image(direct):
                if self.type == 0:
                    if direct == 0:
                        self.image = pygame.transform.scale(mob_img1, (50, 50))
                    if direct == 1:
                        self.image = pygame.transform.scale(mob_img2, (50, 50))
                    if direct == 2:
                        self.image = pygame.transform.scale(mob_img3, (50, 50))
                    if direct == 3:
                        self.image = pygame.transform.scale(mob_img4, (50, 50))
                if self.type == 1:
                    if direct == 0:
                        self.image = pygame.transform.scale(mob_2_img1, (50, 50))
                    if direct == 1:
                        self.image = pygame.transform.scale(mob_2_img2, (50, 50))
                    if direct == 2:
                        self.image = pygame.transform.scale(mob_2_img3, (50, 50))
                    if direct == 3:
                        self.image = pygame.transform.scale(mob_2_img4, (50, 50))
                if self.type == 2:
                    if direct == 0:
                        self.image = pygame.transform.scale(mob_3_img1, (50, 50))
                    if direct == 1:
                        self.image = pygame.transform.scale(mob_3_img2, (50, 50))
                    if direct == 2:
                        self.image = pygame.transform.scale(mob_3_img3, (50, 50))
                    if direct == 3:
                        self.image = pygame.transform.scale(mob_3_img4, (50, 50))
                self.image.set_colorkey(WHITE)

            player_x = player.rect.centerx // 50
            player_y = player.rect.centery // 50

            if self.rect.left == self.locationx + self.step:
                self.direction = randomconverter(self.direction)
                self.locationx = self.rect.left
                self.locationy = self.rect.top
            if self.rect.left == self.locationx - self.step:
                self.direction = randomconverter(self.direction)
                self.locationx = self.rect.left
                self.locationy = self.rect.top
            if self.rect.top == self.locationy + self.step:
                self.direction = randomconverter(self.direction)
                self.locationx = self.rect.left
                self.locationy = self.rect.top
            if self.rect.top == self.locationy - self.step:
                self.direction = randomconverter(self.direction)
                self.locationx = self.rect.left
                self.locationy = self.rect.top

            # if player.autopilot_on or player.destination_on:
            #     if not autopilot(self, player.rect.centerx, player.rect.centery):
            #         self.autopilot_on = False
            #     else:
            #         self.autopilot_on = True
            # if not player.autopilot_on and not player.destination_on:
            #     self.autopilot_on = False

            # if player.autopilot_on or player.destination_on:
            if self.autopilot_on and player.is_detected and self.is_chaser:
                autopilot(self, player.rect.centerx, player.rect.centery)


                if self.direction == 'left':
                    sprite_image(1)
                if self.direction == 'right':
                    sprite_image(2)
                if self.direction == 'up':
                    sprite_image(0)
                if self.direction == 'down':
                    sprite_image(3)


                if player.rect.centery == self.rect.centery and player.is_detected:
                    if player.rect.centerx >= self.rect.centerx:
                        temp = 0
                        for obst in obstacles:
                            if obst.rect.top - 5 <= self.rect.centery <= obst.rect.bottom + 5:
                                if player.rect.right >= obst.rect.right > self.rect.right:
                                    temp = temp + 1
                        if temp == 0:
                            if self.direction == 'right':
                                self.shoot('right')
                                player_shoot('right')
                                change_chaser()
                    if player.rect.centerx < self.rect.centerx:
                        temp = 0
                        for obst in obstacles:
                            if obst.rect.top - 5 <= self.rect.centery <= obst.rect.bottom + 5:
                                if player.rect.right <= obst.rect.right < self.rect.right:
                                    temp = temp + 1
                        if temp == 0:
                            if self.direction == 'left':
                                self.shoot('left')
                                player_shoot('left')
                                change_chaser()

                if player.rect.centerx == self.rect.centerx and player.is_detected:
                    if player.rect.centery >= self.rect.centery:
                        temp = 0
                        for obst in obstacles:
                            if obst.rect.left - 5 <= self.rect.centerx <= obst.rect.right + 5:
                                if player.rect.bottom >= obst.rect.bottom > self.rect.bottom:
                                    temp = temp + 1
                        if temp == 0:
                            if self.direction == 'down':
                                self.shoot('down')
                                player_shoot('down')
                                change_chaser()

                    if player.rect.centery < self.rect.centery:
                        temp = 0
                        for obst in obstacles:
                            if obst.rect.left - 5 <= self.rect.centerx <= obst.rect.right + 5:
                                if player.rect.bottom <= obst.rect.bottom < self.rect.bottom:
                                    temp = temp + 1
                        if temp == 0:
                            if self.direction == 'up':
                                self.shoot('up')
                                player_shoot('up')
                                change_chaser()




            if not self.autopilot_on or (self.autopilot_on and not player.is_detected) or not self.is_chaser:

                if pygame.time.get_ticks() >= self.crashtime + self.crashtime_step:
                    if self.direction == 'right' and self.rect.left < \
                            self.locationx + self.step and self.playerdirection != 'vertical':
                        sprite_image(2)
                        self.rect.left += self.speed
                    elif self.direction == 'left' and self.rect.left > \
                            self.locationx - self.step and self.playerdirection != 'vertical':
                        sprite_image(1)
                        self.rect.left += -self.speed
                    elif self.direction == 'up' and self.rect.top < \
                            self.locationy + self.step and self.playerdirection != 'horizontal':
                        sprite_image(0)
                        self.rect.top += -self.speed
                    elif self.direction == 'down' and self.rect.top > \
                            self.locationy - self.step and self.playerdirection != 'horizontal':
                        sprite_image(3)
                        self.rect.top += self.speed



                if self.rect.right > WIDTH:
                    self.crashtime = pygame.time.get_ticks()
                    self.rect.right = WIDTH
                    self.direction = randomconverter(self.direction)
                    self.locationx = self.rect.left
                    self.locationy = self.rect.top
                if self.rect.top < 50:
                    self.crashtime = pygame.time.get_ticks()
                    self.rect.top = 50
                    self.direction = randomconverter(self.direction)
                    self.locationx = self.rect.left
                    self.locationy = self.rect.top
                if self.rect.left < 0:
                    self.crashtime = pygame.time.get_ticks()
                    self.rect.left = 0
                    self.direction = randomconverter(self.direction)
                    self.locationx = self.rect.left
                    self.locationy = self.rect.top
                if self.rect.bottom > HEIGHT:
                    self.crashtime = pygame.time.get_ticks()
                    self.rect.bottom = HEIGHT
                    self.direction = randomconverter(self.direction)
                    self.locationx = self.rect.left
                    self.locationy = self.rect.top

            if player.rect.centery - 25 <= self.rect.centery <= player.rect.centery + 25 \
                    and player.safe_location != (player_x, player_y) and player.is_detected:
                if player.rect.x >= self.rect.centerx:
                    temp = 0
                    for obst in obstacles:
                        if obst.rect.top - 5 <= self.rect.centery <= obst.rect.bottom + 5:
                            if player.rect.right >= obst.rect.right > self.rect.right:
                                temp = temp + 1
                    if temp == 0:
                        self.autopilot_on = False
                        self.playerdirection = 'horizontal'
                        sprite_image(2)
                        self.shoot('right')
                        player_shoot('right')
                        change_chaser()
                    else:
                        self.autopilot_on = True
                if player.rect.centerx < self.rect.centerx:
                    temp = 0
                    for obst in obstacles:
                        if obst.rect.top - 5 <= self.rect.centery <= obst.rect.bottom + 5:
                            if player.rect.right <= obst.rect.right < self.rect.right:
                                temp = temp + 1
                    if temp == 0:
                        self.autopilot_on = False
                        self.playerdirection = 'horizontal'
                        sprite_image(1)
                        self.shoot('left')
                        player_shoot('left')
                        change_chaser()
                    else:
                        self.autopilot_on = True



            elif player.rect.centerx - 25 <= self.rect.centerx <= player.rect.centerx + 25 \
                    and player.safe_location != (player_x, player_y) and player.is_detected:
                if player.rect.centery >= self.rect.centery:
                    temp = 0
                    for obst in obstacles:
                        if obst.rect.left - 5 <= self.rect.centerx <= obst.rect.right + 5:
                            if player.rect.bottom >= obst.rect.bottom > self.rect.bottom:
                                temp = temp + 1
                    if temp == 0:
                        self.autopilot_on = False
                        self.playerdirection = 'vertical'
                        sprite_image(3)
                        self.shoot('down')
                        player_shoot('down')
                        change_chaser()
                    else:
                        self.autopilot_on = True
                if player.rect.centery < self.rect.centery:
                    temp = 0
                    for obst in obstacles:
                        if obst.rect.left - 5 <= self.rect.centerx <= obst.rect.right + 5:
                            if player.rect.bottom <= obst.rect.bottom < self.rect.bottom:
                                temp = temp + 1
                    if temp == 0:
                        self.autopilot_on = False
                        self.playerdirection = 'vertical'
                        sprite_image(0)
                        self.shoot('up')
                        player_shoot('up')
                        change_chaser()
                    else:
                        self.autopilot_on = True
            else:
                self.playerdirection = ' '
                self.autopilot_on = True




        def shoot(self, direction):
            if pygame.time.get_ticks() >= self.shottime + self.cooldown:
                self.shottime = pygame.time.get_ticks()
                bullet = Bullet(self.rect.top, self.rect.bottom,
                                self.rect.centerx, self.rect.centery, self.rect.right,
                                self.rect.left, direction, self.bulletspeed)
                all_sprites.add(bullet)
                enemy_bullets.add(bullet)
                enemy_shoot_sound.play()

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, top, bottom, centerx, centery, right, left, direction, speed):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(bullet1_img, (10, 15))
            self.rect = self.image.get_rect()
            self.image.set_colorkey(WHITE)
            self.rect.top = top
            self.rect.centerx = centerx
            self.speedy = 0
            self.speedx = 0
            if direction == 'left':
                self.image = pygame.transform.scale(bullet2_img, (15, 10))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.left = left
                self.rect.centery = centery
                self.speedy = 0
                self.speedx = -speed
            if direction == 'right':
                self.image = pygame.transform.scale(bullet3_img, (15, 10))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.right = right
                self.rect.centery = centery
                self.speedy = 0
                self.speedx = speed
            if direction == 'up':
                self.image = pygame.transform.scale(bullet1_img, (10, 15))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.centerx = centerx
                self.rect.top = top
                self.speedx = 0
                self.speedy = -speed
            if direction == 'down':
                self.image = pygame.transform.scale(bullet4_img, (10, 15))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.centerx = centerx
                self.rect.bottom = bottom
                self.speedx = 0
                self.speedy = speed

        def update(self):
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.bottom > HEIGHT or self.rect.top < 50:
                self.kill()
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.kill()

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self, x, y, d=False):
            pygame.sprite.Sprite.__init__(self)
            if not d:
                self.image = pygame.transform.scale(obstacle_img1, (50, 50))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
            if d:
                self.image = pygame.transform.scale(obstacle_img2, (50, 50))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
            self.rect.top = y
            self.rect.left = x
            self.destructibility = d

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, centerx, centery):
            pygame.sprite.Sprite.__init__(self)
            self.image = explosion_anim[0]
            self.rect = self.image.get_rect()
            self.rect.centerx = centerx
            self.rect.centery = centery
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
    class Respawn(pygame.sprite.Sprite):
        def __init__(self, left, top):
            pygame.sprite.Sprite.__init__(self)
            self.image = cross_img
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.top = top

    class Destination(pygame.sprite.Sprite):
        def __init__(self, left, top):
            pygame.sprite.Sprite.__init__(self)
            self.image = destination_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.top = top

        def update(self):
            if not player.destination_on:
                self.kill()

    def randomconverter(direction):
        i = 0
        number = random.randrange(1, 5)
        temp = direction
        while True and i < 10:
            i = i + 1
            if temp == direction:
                if number == 1:
                    temp = 'left'
                if number == 2:
                    temp = 'right'
                if number == 3:
                    temp = 'up'
                if number == 4:
                    temp = 'down'
            else:
                break
        return temp

    def random_obstacles(number, destructibility):
        if not random_map:
            for obj in const.obstacle_list:
                obst = Obstacle(obj.__getitem__(0), obj.__getitem__(1), False)
                obstacles.add(obst)
                all_sprites.add(obst)
        else:
            i = 0
            while i < number:
                locationx = random.randrange(0, WIDTH / 50)
                locationy = random.randrange(1, HEIGHT / 50)
                temp = 0
                if (locationx, locationy) in free_location or (locationx, locationy) == player_coordinates:
                    temp = 1
                elif temp == 0:
                    for obst in obstacles:
                        if obst.rect.left == locationx * 50 and obst.rect.top == locationy * 50:
                            temp = 1
                            break
                if temp == 0:
                    obst = Obstacle(locationx * 50, locationy * 50, destructibility)
                    obstacles.add(obst)
                    all_sprites.add(obst)
                    j = 1
                    while j < free_location.__len__():
                        path = DFS_alg.Search_Pass(create_graph(), create_vertex()[free_location[0]],
                                                   create_vertex()[free_location[j]])
                        j += 1
                        if path.__len__() == 0:
                            temp = 1
                            break
                    if temp == 0:
                        i = i + 1
                    else:
                        obstacles.remove(obst)
                        all_sprites.remove(obst)





    font_name = pygame.font.match_font('arial')

    def draw_text(surf, text, size, x, y, colour):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


    def draw_lives(surf, x, y, lives, img):
        if lives < 6:
            for i in range(lives):
                img_rect = img.get_rect()
                img_rect.x = x - 15 * i
                img_rect.y = y
                surf.blit(img, img_rect)
        else:
            draw_text(screen, str(player.lives), 25, x - 25, y - 3, GREEN)
            img_rect = img.get_rect()
            img_rect.x = x - 10
            img_rect.y = y
            surf.blit(img, img_rect)

    def create_vertex():
        vertex = dict()
        if not random_map:
            vertex = const.vertex_list
        else:
            count = 0
            for j in range(1, int(HEIGHT / 50)):
                for i in range(int(WIDTH / 50)):
                    temp = False
                    for obst in obstacles:
                        if obst.rect.left == i * 50 and obst.rect.top == j * 50:
                            temp = True
                            break
                    if not temp:
                        vertex[i, j] = count
                        count += 1
        return vertex

    def create_graph():
        graph = defaultdict(list)
        if not random_map:
            graph = const.graph
        else:
            temp = create_vertex()
            nodes = list()

            for obj in temp:
                if temp.__contains__((obj[0] + 1, obj[1])):
                    nodes.append((temp[obj], temp[(obj[0] + 1, obj[1])]))
                    nodes.append((temp[(obj[0] + 1, obj[1])], temp[obj]))
                if temp.__contains__((obj[0], obj[1] + 1)):
                    nodes.append((temp[obj], temp[(obj[0], obj[1] + 1)]))
                    nodes.append((temp[(obj[0], obj[1] + 1)], temp[obj]))
            for item in nodes:
                graph[item.__getitem__(0)].append(item.__getitem__(1))

        return graph

    def show_go_screen():
        screen.blit(back_img, back_img_rect)
        draw_text(screen, "Your score: " + str(player.points), 64, WIDTH / 2, HEIGHT / 7, BLACK)
        draw_text(screen, "Remember: arrow keys to move", 30,
                  WIDTH / 2, HEIGHT / 2, RED)
        draw_text(screen, "Space to fire, Escape to pause", 30,
                  WIDTH / 2, HEIGHT / 2 + 30, RED)
        draw_text(screen, "Press Backspace to begin", 30, WIDTH / 2, HEIGHT * 3 / 4 + 50, WHITE)
        pygame.display.flip()

        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                    waiting = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:

                        return True
                        # waiting = False

    def autopilot(obj1, x1, y1):
        speed = obj1.speed
        result = list()
        if pygame.time.get_ticks() >= obj1.autopilot_time + obj1.autopilot_pause:


            obj1.autopilot_time = pygame.time.get_ticks()

            obj1.vertex_list = create_vertex()
            x = obj1.vertex_list[(obj1.rect.centerx // 50, obj1.rect.centery // 50)]
            y = obj1.vertex_list[(x1 // 50, y1 // 50)]
            obj1.autopilot_path = A_star_alg.astar(create_graph(), x, y)



        if (obj1.autopilot_path.__len__() != 0):
            for vertex in obj1.autopilot_path:
                for item in obj1.vertex_list:
                    if obj1.vertex_list[item] == vertex:
                        result.append((item.__getitem__(0), item.__getitem__(1)))
            if result.__len__() > 1:
                try:
                    number = result.index((obj1.rect.centerx // 50, obj1.rect.centery // 50))
                    if result[number].__getitem__(0) == result[number + 1].__getitem__(0):
                        if obj1.rect.left < result[number].__getitem__(0) * 50:
                            obj1.direction = 'right'
                            obj1.rect.centerx += speed
                        elif obj1.rect.left > result[number].__getitem__(0) * 50:
                            obj1.direction = 'left'
                            obj1.rect.centerx -= speed
                        elif obj1.rect.left == result[number + 1].__getitem__(0) * 50:
                            if obj1.rect.top < result[number + 1].__getitem__(1) * 50:
                                obj1.direction = 'down'
                                obj1.rect.centery += speed
                            else:
                                obj1.direction = 'up'
                                obj1.rect.centery -= speed

                    elif result[number].__getitem__(1) == result[number + 1].__getitem__(1):
                        if obj1.rect.top < result[number].__getitem__(1) * 50:
                            obj1.direction = 'down'
                            obj1.rect.centery += speed
                        elif obj1.rect.top > result[number].__getitem__(1) * 50:
                            obj1.direction = 'up'
                            obj1.rect.centery -= speed
                        elif obj1.rect.top == result[number + 1].__getitem__(1) * 50:
                            if obj1.rect.left < result[number + 1].__getitem__(0) * 50:
                                obj1.direction = 'right'
                                obj1.rect.centerx += speed
                            else:
                                obj1.direction = 'left'
                                obj1.rect.centerx -= speed
                    return True
                except:
                    return True

        else:
            return False

    def destination_creator():
        while True:

            x = random.randrange(15)
            y = random.randrange(1, 12)
            temp = 0
            for obst in obstacles:
                if (obst.rect.left // 50, obst.rect.top // 50) == (x, y):
                    temp = 1
                    break
            if temp == 0:
                i = player.rect.left//50
                j = player.rect.top//50
                tmp_path = BFS_alg.Search_Pass(create_graph(), create_vertex()[x, y], create_vertex()[i, j])
                if tmp_path.__len__() > destination:
                    dest = Destination(x*50, y*50)
                    destinations.add(dest)
                    all_sprites.add(dest)
                    player.destination_coordinates = (x, y)
                    break



    def mob_location_creator(number):
        result = list()
        if not random_map:
            result = const.respawn_list
        else:
            count = 0
            while count < number:
                x = random.randrange(15)
                y = random.randrange(1, 12)
                if not (x, y) == player_coordinates and (x * 50, y * 50) not in result:
                    temp = 0
                    for obst in obstacles:
                        if (obst.rect.left // 50, obst.rect.top // 50) == (x, y):
                            temp = 1
                            break
                    if temp == 0 and BFS_alg.Search_Pass(create_graph(), create_vertex()[x, y],
                                                         create_vertex()[player_coordinates]).__len__() > 6:
                        result.append((x * 50, y * 50))
                        count += 1
        return result


    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    random_obstacles(solid_obstacles, False)
    random_obstacles(destructible_obstacles, True)
    mobs_location = mob_location_creator(respawn_number)
    destinations = pygame.sprite.Group()
    for obj in mobs_location:
        x = obj.__getitem__(0)
        y = obj.__getitem__(1)
        resp = Respawn(x, y)
        all_sprites.add(resp)


    all_sprites.add(obstacles)
    player = Player()
    all_sprites.add(player)
    # gh = Destination(0, 100)
    # destinations.add(dest)
    # all_sprites.add(gh)

    fo = create_vertex()


    for i in range(chaser_mob):
        count = i
        n = random.randrange(0, mobs_location.__len__())
        if mobs_location.__len__() == count:
            count = 0
        m = Mob(mobs_location[count].__getitem__(0), mobs_location[count].__getitem__(1), 2)
        all_sprites.add(m)
        mobs.add(m)
    for i in range(random_mob):
        count = i
        n = random.randrange(0, mobs_location.__len__())
        if mobs_location.__len__() == count:
            count = 0
        m = Mob(mobs_location[count].__getitem__(0), mobs_location[count].__getitem__(1), 0)
        all_sprites.add(m)
        mobs.add(m)

    game_over = False
    running = True
    esc_waiting = False

    while running:
        screen.fill(BLACK)
        all_sprites.draw(screen)
        clock.tick(FPS)
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if keystate[pygame.K_SPACE]:
                if player.is_detected and not player.autopilot_on:
                    player.shoot()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if player.is_detected:
                        player.is_detected = False
                    else:
                        player.is_detected = True
                if event.key == pygame.K_a:
                    for item in mobs:
                        item.is_chaser = True


                if event.key == pygame.K_g:
                    if player.destination_on:
                        player.destination_on = False
                        # player.god_mode = False
                        god_mode_off.play()
                    else:
                        # destination_creator()
                        player.destination_on = True
                        # player.god_mode = True
                        # player.autopilot_on = False
                        # player.destination_on = False
                        god_mode_on.play()

                if event.key == pygame.K_ESCAPE:
                    count = 0
                    alg_number = 0
                    z_pressed = False
                    esc_waiting = True
                    while esc_waiting:

                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                esc_waiting = False
                                running = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    esc_waiting = False
                                    main()
                                    return
                                # if event.key == pygame.K_z:
                                #     z_pressed = True
                                #     alg_number += 1
                                #     if alg_number == 3:
                                #         alg_number = 0
                                #     alg_name = ''
                                #     if alg_number == 0:
                                #         alg_name = 'BFS Algorithm'
                                #     if alg_number == 1:
                                #         alg_name = 'DFS Algorithm'
                                #     if alg_number == 2:
                                #         alg_name = 'UCS Algorithm'
                                #     screen.blit(background, background_rect)
                                #     all_sprites.draw(screen)
                                #     screen.blit(panel, panel_rect)
                                #     draw_text(screen, alg_name, 30, WIDTH / 4, 5, GREEN)
                                #     draw_text(screen, 'score: ' + str(player.points), 30, WIDTH / 2, 5, RED)
                                #     draw_lives(screen, WIDTH - 100, 5, player.lives, player_img_mini)
                                #     pygame.display.flip()
                                #
                                # if event.key == pygame.K_RIGHT and z_pressed:
                                #     screen.blit(background, background_rect)
                                #     all_sprites.draw(screen)
                                #     screen.blit(panel, panel_rect)
                                #     draw_text(screen, alg_name, 30, WIDTH / 4, 5, GREEN)
                                #     draw_text(screen, 'score: ' + str(player.points), 30, WIDTH / 2, 5, RED)
                                #     draw_lives(screen, WIDTH - 100, 5, player.lives, player_img_mini)
                                #
                                #     if mobs.sprites().__len__() == count:
                                #         count = 0
                                #     x = create_vertex()[(player.rect.centerx // 50, player.rect.centery // 50)]
                                #     i = mobs.sprites()[count].rect.centerx
                                #     j = mobs.sprites()[count].rect.centery
                                #     draw_text(screen, 'o', 40, i, j - 27, GREEN)
                                #     draw_text(screen, '+', 40, i, j - 25, GREEN)
                                #     y = create_vertex()[(i // 50, j // 50)]
                                #     count = count + 1
                                #     temp_path = list()
                                #     if alg_number == 0:
                                #         temp_path = BFS_alg.Search_Pass(create_graph(), x, y)
                                #     if alg_number == 1:
                                #         temp_path = DFS_alg.Search_Pass(create_graph(), x, y)
                                #     if alg_number == 2:
                                #         temp_path = UCS_alg.Search_Pass(create_graph(), x, y)
                                #
                                #     if (temp_path.__len__() != 0):
                                #         temp_list = list()
                                #         for obj in temp_path:
                                #             temp = create_vertex()
                                #             for item in temp:
                                #                 if obj == temp[item]:
                                #                     temp_list.append(item)
                                #         counter = 0
                                #         while counter < temp_list.__len__() - 1:
                                #             i = temp_list[counter].__getitem__(0) * 50
                                #             j = temp_list[counter].__getitem__(1) * 50 + 50
                                #             if temp_list[counter].__getitem__(0) > temp_list[counter+1].__getitem__(0):
                                #                 draw_text(screen, '←', 35, i + 25, j - 50, GREEN)
                                #             if temp_list[counter].__getitem__(0) < temp_list[counter+1].__getitem__(0):
                                #                 draw_text(screen, '→', 35, i + 25, j - 50, GREEN)
                                #             if temp_list[counter].__getitem__(1) > temp_list[counter+1].__getitem__(1):
                                #                 draw_text(screen, '↑', 35, i + 25, j - 50, GREEN)
                                #             if temp_list[counter].__getitem__(1) < temp_list[counter+1].__getitem__(1):
                                #                 draw_text(screen, '↓', 35, i + 25, j - 50, GREEN)
                                #             counter += 1
                                #         pygame.display.flip()
                                #     else:
                                #         draw_text(screen, 'path does not exist', 30,
                                #                   WIDTH / 5, 5, GREEN)
                                #         pygame.display.flip()

                                if event.key == pygame.K_ESCAPE:
                                    esc_waiting = False

        all_sprites.update()

        bullethit = pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)
        if bullethit:
            for key in bullethit:
                bullets_hit.play()
                expl = Explosion(key.rect.centerx, key.rect.centery)
                all_sprites.add(expl)
        obstaclehit = pygame.sprite.groupcollide(bullets, obstacles, True, False)
        # if obstaclehit:
        #     for obst in obstaclehit.values():
        #         if obst[0].destructibility:
        #             obst[0].kill()
        #             obstacles.remove(obst[0])
        #             all_sprites.remove(obst[0])

        obstaclehit1 = pygame.sprite.groupcollide(enemy_bullets, obstacles, True, False)
        # if obstaclehit1:
        #     for obst in obstaclehit1.values():
        #         if obst[0].destructibility:
        #             obst[0].kill()
        #             obstacles.remove(obst[0])
        #             all_sprites.remove(obst[0])
        obstaclecrash = pygame.sprite.spritecollide(player, obstacles, False)
        if obstaclecrash:
            for key in obstaclecrash:
                if player.direction == 'left':
                    if 10 >= (key.rect.bottom - player.rect.top) > 0:
                        player.rect.top = key.rect.bottom
                    if 10 >= (player.rect.bottom - key.rect.top) > 0:
                        player.rect.bottom = key.rect.top
                    player.rect.x = player.rect.x + player.rect.size[0] - (player.rect.right - key.rect.right)
                if player.direction == 'right':
                    if 10 >= (key.rect.bottom - player.rect.top) > 0:
                        player.rect.top = key.rect.bottom
                    if 10 >= (player.rect.bottom - key.rect.top) > 0:
                        player.rect.bottom = key.rect.top
                    player.rect.x = player.rect.x - player.rect.size[0] - (player.rect.left - key.rect.left)
                if player.direction == 'up':
                    if 10 >= (key.rect.right - player.rect.left) > 0:
                        player.rect.left = key.rect.right
                    if 10 >= (player.rect.right - key.rect.left) > 0:
                        player.rect.right = key.rect.left
                    player.rect.y = player.rect.y + player.rect.size[1] - (player.rect.bottom - key.rect.bottom)
                if player.direction == 'down':
                    if 10 >= (key.rect.right - player.rect.left) > 0:
                        player.rect.left = key.rect.right
                    if 10 >= (player.rect.right - key.rect.left) > 0:
                        player.rect.right = key.rect.left
                    player.rect.y = player.rect.y - player.rect.size[1] - (player.rect.top - key.rect.top)

        obstaclecrash1 = pygame.sprite.groupcollide(mobs, obstacles, False, False)
        if obstaclecrash1:
            for key in obstaclecrash1:
                for obst in obstaclecrash1.values():
                    for en in obst:
                        key.crashtime = pygame.time.get_ticks()
                        if key.direction == 'left':
                            key.direction = randomconverter(key.direction)
                            key.rect.left = en.rect.right
                            key.locationx = key.rect.left
                            key.locationy = key.rect.top
                        elif key.direction == 'right':
                            key.direction = randomconverter(key.direction)
                            key.rect.left = en.rect.left-50
                            key.locationx = key.rect.left
                            key.locationy = key.rect.top
                        elif key.direction == 'up':
                            key.direction = randomconverter(key.direction)
                            key.rect.top = en.rect.bottom
                            key.locationx = key.rect.left
                            key.locationy = key.rect.top
                        elif key.direction == 'down':
                            key.direction = randomconverter(key.direction)
                            key.rect.top = en.rect.top - 50
                            key.locationx = key.rect.left
                            key.locationy = key.rect.top
                        break
                    break
                break

        mobhits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        if mobhits:
            for key in mobhits:
                enemy_hit.play()
                if not player.god_mode:
                    player.points = player.points + 1
                expl = Explosion(key.rect.centerx, key.rect.centery)
                all_sprites.add(expl)
                break

        # for hit in mobhits:
        #     n = random.randrange(0, mobs_location.__len__())
        #     m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1), random.choice([0, 1, 2]))
        #     all_sprites.add(m)
        #     mobs.add(m)

        ram = pygame.sprite.spritecollide(player, mobs, False)
        if ram:
            for key in ram:
                expl = Explosion(key.rect.centerx, key.rect.centery)
                all_sprites.add(expl)
                enemy_hit.play()
                if player.is_detected and not player.god_mode:
                    player.points = player.points + 1
                    player_hit.play()
                mobs.remove(key)
                all_sprites.remove(key)
                # n = random.randrange(0, mobs_location.__len__())
                # m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1), random.choice([0, 1, 2]))
                # all_sprites.add(m)
                # mobs.add(m)
            if not player.god_mode and player.is_detected:
                player.lives = player.lives - 1

            if player.lives > 0:

                if not player.autopilot_on and not player.god_mode and not player.destination_on:
                    all_sprites.remove(enemy_bullets)
                    enemy_bullets.empty()
                    player.safe_location = player_coordinates
                    player.is_detected = False
                    player.rect.left = player_coordinates.__getitem__(0) * 50
                    player.rect.top = player_coordinates.__getitem__(1) * 50
                    player.direction = 'up'
                    player.image = pygame.transform.scale(player_img1, (50, 50))
                    player.image.set_colorkey(WHITE)
                    for item in mobs:
                        if item.type == 1:
                            item.is_chaser = False
            else:
                # if player.destination_on:
                #     all_sprites.remove(enemy_bullets)
                #     enemy_bullets.empty()
                #     player.safe_location = player_coordinates
                #     player.is_detected = False
                #     player.destination_on = False
                #     player.lives = player_lives
                #     player.rect.left = player_coordinates.__getitem__(0) * 50
                #     player.rect.top = player_coordinates.__getitem__(1) * 50
                #     player.direction = 'up'
                #     player.image = pygame.transform.scale(player_img1, (50, 50))
                #     player.image.set_colorkey(WHITE)
                # else:
                if minimax:
                    alg = 'minimax'
                else:
                    alg = 'expectimax'
                with open(r'statistic.csv', 'a', newline='') as csvfile:
                    columns = ["win_or_lose", "time", "score", "alg"]
                    writer = csv.DictWriter(csvfile, fieldnames=columns)
                    result = {"win_or_lose": 0, "time": pygame.time.get_ticks(), "score": player.points, "alg": alg}
                    writer.writerow(result)
                    temp = show_go_screen()
                if not temp:
                    return
                if temp:
                    main()
                    return
                    break



        destination_achieved = pygame.sprite.spritecollide(player, destinations, True)
        if destination_achieved:
            player.destination_points += 1

        playerhits = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_rect_ratio(0.9))
        if playerhits and not player.god_mode:
            player_hit.play()
            expl = Explosion(player.rect.centerx, player.rect.centery)
            all_sprites.add(expl)
            for p in playerhits:
                if playerhits:
                    if player.is_detected:
                        player.lives = player.lives - 1
                    if player.lives > 0:
                        if not player.autopilot_on and not player.destination_on:
                            all_sprites.remove(enemy_bullets)
                            enemy_bullets.empty()
                            player.safe_location = player_coordinates
                            player.is_detected = False
                            player.rect.left = player_coordinates.__getitem__(0) * 50
                            player.rect.top = player_coordinates.__getitem__(1) * 50
                            player.direction = 'up'
                            player.image = pygame.transform.scale(player_img1, (50, 50))
                            player.image.set_colorkey(WHITE)
                            for item in mobs:
                                if item.type == 1:
                                    item.is_chaser = False
                        break
                    else:
                        # if player.destination_on:
                        #     all_sprites.remove(enemy_bullets)
                        #     enemy_bullets.empty()
                        #     player.safe_location = player_coordinates
                        #     player.is_detected = False
                        #     player.destination_on = False
                        #     player.lives = player_lives
                        #     player.rect.left = player_coordinates.__getitem__(0) * 50
                        #     player.rect.top = player_coordinates.__getitem__(1) * 50
                        #     player.direction = 'up'
                        #     player.image = pygame.transform.scale(player_img1, (50, 50))
                        #     player.image.set_colorkey(WHITE)
                        # else:
                        if minimax:
                            alg = 'minimax'
                        else:
                            alg = 'expectimax'
                        with open(r'statistic.csv', 'a', newline='') as csvfile:
                            columns = ["win_or_lose", "time", "score", "alg"]
                            writer = csv.DictWriter(csvfile, fieldnames=columns)
                            result = {"win_or_lose": 0, "time": pygame.time.get_ticks(), "score": player.points, "alg": alg}
                            writer.writerow(result)

                            temp = show_go_screen()
                        if not temp:
                            return
                        if temp:
                            main()
                            return
                            break


        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        screen.blit(panel, panel_rect)
        # if player.god_mode:
        #     draw_text(screen, 'God mode', 30, WIDTH / 2 - 250, 5, GREEN)
        # if player.autopilot_on:
        #     draw_text(screen, 'Autopilot mode', 30, WIDTH / 2 - 250, 5, GREEN)
        # if player.destination_on:
        #     draw_text(screen, 'Destination mode', 30, WIDTH / 2 - 250, 5, GREEN)
        draw_text(screen, 'score: ' + str(player.points), 30, WIDTH / 2, 5, RED)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_img_mini)
        pygame.display.flip()

    pygame.quit()


main()
