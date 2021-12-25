from collections import defaultdict

import pygame
import random
import pygame.freetype
from os import path
import sys
import os
import BFS_alg
import DFS_alg
import A_star_alg
import const


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

# //cheats



# //cheats

console_remind = []
console_text = []
console_text.append(("Welcome to console!", const.YELLOW))

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

    # destination_path = 'sprite_images/diamond.tga'
    # cross_path = 'sprite_images/krest.jpg'
    # background_path = 'sprite_images/ground02.bmp'
    # player_img1_path = 'sprite_images/pla1.bmp'
    # player_img2_path = 'sprite_images/pla2.bmp'
    # player_img3_path = 'sprite_images/pla3.bmp'
    # player_img4_path = 'sprite_images/pla4.bmp'
    # obstacle_img1_path = 'sprite_images/block_02.bmp'
    # obstacle_img2_path = 'sprite_images/block_08.bmp'
    # bullet1_img_path = 'sprite_images/bullet1.png'
    # bullet2_img_path = 'sprite_images/bullet2.png'
    # bullet3_img_path = 'sprite_images/bullet3.png'
    # bullet4_img_path = 'sprite_images/bullet4.png'
    # s_bullet1_img_path = 'sprite_images/s_bullet1.png'
    # s_bullet2_img_path = 'sprite_images/s_bullet2.png'
    # s_bullet3_img_path = 'sprite_images/s_bullet3.png'
    # s_bullet4_img_path = 'sprite_images/s_bullet4.png'
    # mob_3_img1_path = 'sprite_images/s1.bmp'
    # mob_3_img2_path = 'sprite_images/s2.bmp'
    # mob_3_img3_path = 'sprite_images/s3.bmp'
    # mob_3_img4_path = 'sprite_images/s4.bmp'
    # mob_2_img1_path = 'sprite_images/t1.bmp'
    # mob_2_img2_path = 'sprite_images/t2.bmp'
    # mob_2_img3_path = 'sprite_images/t3.bmp'
    # mob_2_img4_path = 'sprite_images/t4.bmp'
    # mob_img1_path = 'sprite_images/v1.bmp'
    # mob_img2_path = 'sprite_images/v2.bmp'
    # mob_img3_path = 'sprite_images/v3.bmp'
    # mob_img4_path = 'sprite_images/v4.bmp'
    # back_img_path = 'sprite_images/i_background.jpg'
    # panel_path = 'sprite_images/panel.bmp'
    # player_img_mini_path = 'sprite_images/pla1_mini.bmp'
    # img_exp0_path = 'sprite_images/regularExplosion00.png'
    # img_exp1_path = 'sprite_images/regularExplosion01.png'
    # img_exp2_path = 'sprite_images/regularExplosion02.png'
    # img_exp3_path = 'sprite_images/regularExplosion03.png'
    # img_exp4_path = 'sprite_images/regularExplosion04.png'
    # img_exp5_path = 'sprite_images/regularExplosion05.png'
    # img_exp6_path = 'sprite_images/regularExplosion06.png'
    # img_exp7_path = 'sprite_images/regularExplosion07.png'
    # img_exp8_path = 'sprite_images/regularExplosion08.png'
    # shoot_sound_path = 'sounds/shoot.wav'
    # enemy_shoot_sound_path = 'sounds/enemy_shoot.wav'
    # enemy_hit_path = 'sounds/enemy_hit.wav'
    # god_mode_on_path = 'sounds/Powerup.wav'
    # god_mode_off_path = 'sounds/Powerup1.wav'
    # bullets_hit_path = 'sounds/Hit_Hurt.wav'
    # player_hit_path = 'sounds/player_kill.wav'
    # mask_path = 'sprite_images/mask.bmp'
    # god_pict_path = 'sprite_images/god.png'
    # rate_img_path = 'sprite_images/rate.png'
    # b_speed_img_path = 'sprite_images/bullet_speed.jpg'
    # super_bullet_img_path = 'sprite_images/super_bullet.png'
    # pl_speed_img_path = 'sprite_images/speed.jpg'
    # diguise_img_path = 'sprite_images/disguise.jpg'
    # no_walls_img_path = 'sprite_images/no_blocks.bmp'



    mask_path = resource_path(os.path.join('sprite_images', 'mask.bmp'))
    destination_path = resource_path(os.path.join('sprite_images', 'diamond.tga'))
    cross_path = resource_path(os.path.join('sprite_images', 'krest.jpg'))
    background_path = resource_path(os.path.join('sprite_images', 'ground02.bmp'))
    player_img1_path = resource_path(os.path.join('sprite_images', 'pla1.bmp'))
    player_img2_path = resource_path(os.path.join('sprite_images', 'pla2.bmp'))
    player_img3_path = resource_path(os.path.join('sprite_images', 'pla3.bmp'))
    player_img4_path = resource_path(os.path.join('sprite_images', 'pla4.bmp'))
    obstacle_img1_path = resource_path(os.path.join('sprite_images', 'block_02.bmp'))
    obstacle_img2_path = resource_path(os.path.join('sprite_images', 'block_08.bmp'))
    bullet1_img_path = resource_path(os.path.join('sprite_images', 'bullet1.png'))
    bullet2_img_path = resource_path(os.path.join('sprite_images', 'bullet2.png'))
    bullet3_img_path = resource_path(os.path.join('sprite_images', 'bullet3.png'))
    bullet4_img_path = resource_path(os.path.join('sprite_images', 'bullet4.png'))
    s_bullet1_img_path = resource_path(os.path.join('sprite_images', 's_bullet1.png'))
    s_bullet2_img_path = resource_path(os.path.join('sprite_images', 's_bullet2.png'))
    s_bullet3_img_path = resource_path(os.path.join('sprite_images', 's_bullet3.png'))
    s_bullet4_img_path = resource_path(os.path.join('sprite_images', 's_bullet4.png'))
    mob_3_img1_path = resource_path(os.path.join('sprite_images', 's1.bmp'))
    mob_3_img2_path = resource_path(os.path.join('sprite_images', 's2.bmp'))
    mob_3_img3_path = resource_path(os.path.join('sprite_images', 's3.bmp'))
    mob_3_img4_path = resource_path(os.path.join('sprite_images', 's4.bmp'))
    mob_2_img1_path = resource_path(os.path.join('sprite_images', 't1.bmp'))
    mob_2_img2_path = resource_path(os.path.join('sprite_images', 't2.bmp'))
    mob_2_img3_path = resource_path(os.path.join('sprite_images', 't3.bmp'))
    mob_2_img4_path = resource_path(os.path.join('sprite_images', 't4.bmp'))
    mob_img1_path = resource_path(os.path.join('sprite_images', 'v1.bmp'))
    mob_img2_path = resource_path(os.path.join('sprite_images', 'v2.bmp'))
    mob_img3_path = resource_path(os.path.join('sprite_images', 'v3.bmp'))
    mob_img4_path = resource_path(os.path.join('sprite_images', 'v4.bmp'))
    back_img_path = resource_path(os.path.join('sprite_images', 'i_background.jpg'))
    panel_path = resource_path(os.path.join('sprite_images', 'panel.bmp'))
    player_img_mini_path = resource_path(os.path.join('sprite_images', 'pla1_mini.bmp'))
    img_exp0_path = resource_path(os.path.join('sprite_images', 'regularExplosion00.png'))
    img_exp1_path = resource_path(os.path.join('sprite_images', 'regularExplosion01.png'))
    img_exp2_path = resource_path(os.path.join('sprite_images', 'regularExplosion02.png'))
    img_exp3_path = resource_path(os.path.join('sprite_images', 'regularExplosion03.png'))
    img_exp4_path = resource_path(os.path.join('sprite_images', 'regularExplosion04.png'))
    img_exp5_path = resource_path(os.path.join('sprite_images', 'regularExplosion05.png'))
    img_exp6_path = resource_path(os.path.join('sprite_images', 'regularExplosion06.png'))
    img_exp7_path = resource_path(os.path.join('sprite_images', 'regularExplosion07.png'))
    img_exp8_path = resource_path(os.path.join('sprite_images', 'regularExplosion08.png'))
    shoot_sound_path = resource_path(os.path.join('sounds', 'shoot.wav'))
    enemy_shoot_sound_path = resource_path(os.path.join('sounds', 'enemy_shoot.wav'))
    enemy_hit_path = resource_path(os.path.join('sounds', 'enemy_hit.wav'))
    god_mode_on_path = resource_path(os.path.join('sounds', 'Powerup.wav'))
    god_mode_off_path = resource_path(os.path.join('sounds', 'Powerup1.wav'))
    bullets_hit_path = resource_path(os.path.join('sounds', 'Hit_Hurt.wav'))
    player_hit_path = resource_path(os.path.join('sounds', 'player_kill.wav'))
    god_pict_path = resource_path(os.path.join('sprite_images', 'god.png'))
    rate_img_path = resource_path(os.path.join('sprite_images', 'rate.png'))
    b_speed_img_path = resource_path(os.path.join('sprite_images', 'bullet_speed.jpg'))
    super_bullet_img_path = resource_path(os.path.join('sprite_images', 'super_bullet.png'))
    pl_speed_img_path = resource_path(os.path.join('sprite_images', 'speed.jpg'))
    disguise_img_path = resource_path(os.path.join('sprite_images', 'disguise.jpg'))
    no_walls_img_path = resource_path(os.path.join('sprite_images', 'no_blocks.bmp'))

    god_img = pygame.image.load(god_pict_path).convert()
    god_img = pygame.transform.scale(god_img, (30, 30))

    rate_img = pygame.image.load(rate_img_path).convert()
    rate_img = pygame.transform.scale(rate_img, (30, 30))

    b_speed_img = pygame.image.load(b_speed_img_path).convert()
    b_speed_img = pygame.transform.scale(b_speed_img, (30, 30))

    super_bullet_img = pygame.image.load(super_bullet_img_path).convert()
    super_bullet_img = pygame.transform.scale(super_bullet_img, (30, 30))

    disguise_img = pygame.image.load(disguise_img_path).convert()
    disguise_img = pygame.transform.scale(disguise_img, (30, 30))

    pl_speed_img = pygame.image.load(pl_speed_img_path).convert()
    pl_speed_img = pygame.transform.scale(pl_speed_img, (30, 30))

    no_walls_img = pygame.image.load(no_walls_img_path).convert()
    no_walls_img = pygame.transform.scale(no_walls_img, (30, 30))

    mask_img = pygame.image.load(mask_path).convert()
    mask_img = pygame.transform.scale(mask_img, (50, 50))

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

    s_bullet1_img = pygame.image.load(s_bullet1_img_path).convert()
    s_bullet2_img = pygame.image.load(s_bullet2_img_path).convert()
    s_bullet3_img = pygame.image.load(s_bullet3_img_path).convert()
    s_bullet4_img = pygame.image.load(s_bullet4_img_path).convert()

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





    respawn_number = 4
    mobs_number = 8
    solid_obstacles = 32
    destructible_obstacles = 60
    player_lives = 10
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
            self.direction = 'up'
            self.cooldown = 1300
            self.shottime = -self.cooldown
            self.bulletspeed = 5
            self.speed = 2
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
            self.destination_on = False
            self.destination_coordinates = (0, 0)
            self.destination_points = 0
            self.mask = False
            self.super_bullet = False
            self.no_walls = False






        def update(self):

            if const.disguise:
                self.mask = True
            if not const.disguise:
                self.mask = False
            if const.no_walls:
                self.no_walls = True
            if not const.no_walls:
                self.no_walls = False
            if const.god_mode:
                self.god_mode = True
            if not const.god_mode:
                self.god_mode = False
            if const.super_bullet:
                self.super_bullet = True
            if not const.super_bullet:
                self.super_bullet = False
            if const.b_pl_speed:
                self.speed = const.cheat_pl_speed
            if not const.b_pl_speed:
                self.speed = const.pl_speed
            if const.b_bul_speed:
                self.bulletspeed = const.cheat_bul_speed
            if not const.b_bul_speed:
                self.bulletspeed = const.bul_speed
            if const.b_cooldown:
                self.cooldown = const.cheat_cooldown
            if not const.b_cooldown:
                self.cooldown = const.cooldown



            # if self.autopilot_on:
            #     self.cooldown = 500
            #     self.bulletspeed = 5
            #     self.speed = 1
            #
            # if self.destination_on:
            #     self.cooldown = 500
            #     self.bulletspeed = 5
            #     self.speed = 1

            # if not self.god_mode and not self.autopilot_on and not self.destination_on:
            #     self.speed = 2
            #     self.cooldown = 1300
            #     self.bulletspeed = 5




            self.speedx = 0
            self.speedy = 0

            def detected():
                if mask.__len__() != 0:
                    self.mask = False
                    all_sprites.remove(mask)
                    mask.empty()
                self.is_detected = True
                self.safe_location = (-1, -1)


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
            # if self.destination_on:
            #     if self.destination_coordinates != (0, 0) and \
            #             not autopilot(player, self.destination_coordinates.__getitem__(0)*50,
            #               self.destination_coordinates.__getitem__(1)*50):
            #         self.destination_coordinates = (0, 0)
            #         player.lives = player_lives
            #         self.destination_on = False
            #     else:
            #         detected()
            #
            # if self.autopilot_on:
            #     temp = 0
            #     for item in mobs.sprites():
            #         if autopilot(player, item.rect.centerx, item.rect.centery):
            #             detected()
            #             temp += 1
            #             break
            #     if temp == 0:
            #         self.autopilot_on = False
            #         player.lives = player_lives

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
                                self.rect.right, self.rect.left, self.direction, self.bulletspeed, player.super_bullet)
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
                        change_chaser()
                        # self.autopilot_on = True
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
                        change_chaser()
                        # self.autopilot_on = True
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
                                self.rect.left, direction, self.bulletspeed, False)
                all_sprites.add(bullet)
                enemy_bullets.add(bullet)
                enemy_shoot_sound.play()

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, top, bottom, centerx, centery, right, left, direction, speed, is_super):
            pygame.sprite.Sprite.__init__(self)
            self.is_super = is_super
            self.image = pygame.transform.scale(bullet1_img, (10, 15))
            self.rect = self.image.get_rect()
            self.image.set_colorkey(WHITE)
            self.rect.top = top
            self.rect.centerx = centerx
            self.speedy = 0
            self.speedx = 0
            if direction == 'left':
                if not self.is_super:
                    self.image = pygame.transform.scale(bullet2_img, (15, 10))
                else:
                    self.image = pygame.transform.scale(s_bullet2_img, (15, 10))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.left = left
                self.rect.centery = centery
                self.speedy = 0
                self.speedx = -speed
            if direction == 'right':
                if not self.is_super:
                    self.image = pygame.transform.scale(bullet3_img, (15, 10))
                else:
                    self.image = pygame.transform.scale(s_bullet3_img, (15, 10))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.right = right
                self.rect.centery = centery
                self.speedy = 0
                self.speedx = speed
            if direction == 'up':
                if not self.is_super:
                    self.image = pygame.transform.scale(bullet1_img, (10, 15))
                else:
                    self.image = pygame.transform.scale(s_bullet1_img, (10, 15))
                self.rect = self.image.get_rect()
                self.image.set_colorkey(WHITE)
                self.rect.centerx = centerx
                self.rect.top = top
                self.speedx = 0
                self.speedy = -speed
            if direction == 'down':
                if not self.is_super:
                    self.image = pygame.transform.scale(bullet4_img, (10, 15))
                else:
                    self.image = pygame.transform.scale(s_bullet4_img, (10, 15))
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
            self.destructibility = d
            self.image = pygame.transform.scale(obstacle_img1, (50, 50))
            self.rect = self.image.get_rect()

            if self.destructibility:
                self.image = pygame.transform.scale(obstacle_img2, (50, 50))
            self.image.set_colorkey(WHITE)

            self.rect.top = y
            self.rect.left = x


        def update(self):
            if not self.destructibility:
                self.image = pygame.transform.scale(obstacle_img1, (50, 50))
            if self.destructibility:
                self.image = pygame.transform.scale(obstacle_img2, (50, 50))

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

    class Mask(pygame.sprite.Sprite):
        def __init__(self, left, top):
            pygame.sprite.Sprite.__init__(self)
            self.image = mask_img
            self.image.set_colorkey(WHITE)
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

    def SwapObstacles():
        for obst in obstacles:
            if obst.destructibility:
                obst.destructibility = False
            else:
                obst.destructibility = True

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
        i = 0
        while i < number:
            locationx = random.randrange(0, WIDTH/50)
            locationy = random.randrange(1, HEIGHT/50)
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

    def draw_icons(surf):
        img_list = []

        if const.god_mode:
            img_list.append(god_img)
        if const.no_walls:
            img_list.append(no_walls_img)
        if const.b_cooldown:
            img_list.append(rate_img)
        if const.b_bul_speed:
            img_list.append(b_speed_img)
        if const.b_pl_speed:
            img_list.append(pl_speed_img)
        if const.super_bullet:
            img_list.append(super_bullet_img)
        if const.disguise:
            img_list.append(disguise_img)
        count = 0
        for img in img_list:
            img_rect = img.get_rect()
            img_rect.x = 50 + 35 * count
            img_rect.y = 10
            surf.blit(img, img_rect)
            count += 1

    def create_vertex():
        vertex = dict()
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
        temp = create_vertex()
        nodes = list()
        graph = defaultdict(list)

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

    def console():
        mouse = False
        mouse_count = 0
        def write_text(text, id):
            if not text == "":
                text_surf = font.render(text, True, WHITE)
                text_rect = text_surf.get_rect()
                text_rect.left = 10
                text_rect.top = id * 20
                screen.blit(text_surf, text_rect)
        el_number = console_remind.__len__()
        clock = pygame.time.Clock()
        text = ''
        console_panel = pygame.image.load(panel_path).convert()
        console_panel.fill(BLACK)
        console_panel = pygame.transform.scale(console_panel, (WIDTH, 300))

        font = pygame.font.SysFont(None, 20)

        input_active = True
        run = True
        while run:
            clock.tick(60)
            fr = console_text.__len__() - 14

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                        run = False
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 4:
                        mouse = True
                        if fr - mouse_count >= 1:
                            mouse_count += 1
                    elif event.button == 5:
                        if mouse_count >= 1:
                            mouse = True
                            mouse_count -= 1
                        else:
                            mouse = False


                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_UP:
                        if el_number > 0:
                            el_number -= 1
                            text = ''
                            text += console_remind[el_number]

                    if event.key == pygame.K_DOWN:
                        if el_number < console_remind.__len__()-1:
                            el_number += 1
                            text = ''
                            text += console_remind[el_number]
                    if event.key == pygame.K_RETURN:
                        mouse = False
                        if not text == '':
                            console_text.append((text, WHITE))
                            console_remind.append(text)
                            el_number = console_remind.__len__()
                        if text == 'no walls':
                            if const.no_walls:
                                const.no_walls = False
                                console_text.append(('no walls: OFF', GREEN))

                            else:
                                const.no_walls = True
                                console_text.append(('no walls: ON', GREEN))
                        elif text == 'god':
                            if const.god_mode:
                                const.god_mode = False
                                console_text.append(('god mode: OFF', GREEN))

                            else:
                                const.god_mode = True
                                console_text.append(('god mode: ON', GREEN))
                        elif text == 'disguise':
                            if const.disguise:
                                const.disguise = False
                                console_text.append(('disguise: OFF', GREEN))

                            else:
                                const.disguise = True
                                console_text.append(('disguise: ON', GREEN))
                        elif text == 'player speed':
                            if const.b_pl_speed:
                                const.b_pl_speed = False
                                console_text.append(('player speed: LOW', GREEN))

                            else:
                                const.b_pl_speed = True
                                console_text.append(('player speed: HIGH', GREEN))
                        elif text == 'bullet speed':
                            if const.b_bul_speed:
                                const.b_bul_speed = False
                                console_text.append(('bullet speed: LOW', GREEN))

                            else:
                                const.b_bul_speed = True
                                console_text.append(('bullet speed: HIGH', GREEN))
                        elif text == 'cooldown':
                            if const.b_cooldown:
                                const.b_cooldown = False
                                console_text.append(('cooldown=1300ms', GREEN))

                            else:
                                const.b_cooldown = True
                                console_text.append(('cooldown=100ms', GREEN))
                        elif text == 'super bullet':
                            if const.super_bullet:
                                const.super_bullet = False
                                console_text.append(('super bullet: OFF', GREEN))

                            else:
                                const.super_bullet = True
                                console_text.append(('super bullet: ON', GREEN))
                        elif text == 'swap blocks':
                            SwapObstacles()
                            console_text.append(('blocks swapped', GREEN))
                        elif text == 'refresh lives':
                            player.lives = player_lives
                            console_text.append(('Lives refreshed', GREEN))
                        elif text == 'help':
                            console_text.append(('COMMANDS:', YELLOW))
                            console_text.append(('"no walls" to ignore blocks while moving the player', YELLOW))
                            console_text.append(('"god" to switch god mode', YELLOW))
                            console_text.append(('"disguise" to enable disguise (press "M" to activate)', YELLOW))
                            console_text.append(('"super bullet" to make the bullet more effective', YELLOW))
                            console_text.append(('"swap blocks" to swap destructible and non-destructible blocks', YELLOW))
                            console_text.append(('"cooldown" to change rate of fire', YELLOW))
                            console_text.append(('"player speed" to change player speed', YELLOW))
                            console_text.append(('"bullet speed" to change bullet speed', YELLOW))
                            console_text.append(('"refresh lives" to  regain player health', YELLOW))
                        else:
                            console_text.append(('invalid input, try "help"', RED))
                        mouse = False
                        mouse_count = 0

                        text = ''


                    elif event.key == pygame.K_BACKSPACE:
                        mouse = False
                        mouse_count = 0
                        text = text[:-1]
                    else:
                        mouse = False
                        mouse_count = 0
                        if text.__len__() < 60:
                            text += event.unicode

                screen.fill(BLACK)
                screen.blit(background, background_rect)
                all_sprites.draw(screen)

                screen.blit(console_panel, console_panel.get_rect())


                counter = 0
                if console_text.__len__() < 15:
                    for line in console_text:
                        line_surf = font.render(line.__getitem__(0), True, line.__getitem__(1))
                        line_rect = line_surf.get_rect()
                        line_rect.left = 10
                        line_rect.top = counter * 20
                        screen.blit(line_surf, line_rect)
                        counter += 1
                    write_text(text, counter)
                else:
                    i = console_text.__len__() - 14
                    j = console_text.__len__()
                    if mouse:
                        if mouse_count > 0:
                            i -= mouse_count
                            j = i + 14
                        elif mouse_count < 0:
                            i += mouse_count
                            j = i + 14
                    while (i < j):
                        obj = console_text[i]
                        line_surf = font.render(obj.__getitem__(0), True, obj.__getitem__(1))
                        line_rect = line_surf.get_rect()
                        line_rect.left = 10
                        line_rect.top = counter * 20
                        screen.blit(line_surf, line_rect)
                        counter += 1
                        i += 1
                    if not mouse:
                        write_text(text, counter)


                pygame.display.flip()


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
        try:
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
                player.is_detected = False
                return False
        except:
            player.is_detected = False
            return  False

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
        count = 0
        while count < number:
            x = random.randrange(15)
            y = random.randrange(1, 12)
            if not (x, y) == player_coordinates and (x * 50, y * 50) not in result:
                temp = 0
                for obst in obstacles:
                    if (obst.rect.left//50, obst.rect.top//50) == (x, y):
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
    mask = pygame.sprite.Group()
    for obj in mobs_location:
        x = obj.__getitem__(0)
        y = obj.__getitem__(1)
        resp = Respawn(x, y)
        all_sprites.add(resp)


    all_sprites.add(obstacles)
    player = Player()
    all_sprites.add(player, mask)


    for i in range(mobs_number):
        n = random.randrange(0, mobs_location.__len__())
        m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1), random.choice([0, 1, 2]))
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
                player.shoot()
                if mask.__len__() != 0:
                    player.mask = False
                    all_sprites.remove(mask)
                    mask.empty()
                player.is_detected = True


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                    console()
                if event.key == pygame.K_m:
                    if mask.__len__() == 0 and player.mask:
                        player.mask = True
                        m = Mask(player.rect.left, player.rect.top)
                        mask.add(m)
                        all_sprites.add(m)
                        player.is_detected = False


                # if event.key == pygame.K_b:
                #     SwapObstacles()

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

        bullethit = pygame.sprite.groupcollide(bullets, enemy_bullets, False, True)
        if bullethit:
            for key in bullethit:
                if not key.is_super:
                    all_sprites.remove(key)
                    bullets.remove(key)
                bullets_hit.play()
                expl = Explosion(key.rect.centerx, key.rect.centery)
                all_sprites.add(expl)
        obstaclehit = pygame.sprite.groupcollide(bullets, obstacles, False, False)
        if obstaclehit:
            for obst in obstaclehit.values():
                if obst[0].destructibility:
                    obst[0].kill()
                    obstacles.remove(obst[0])
                    all_sprites.remove(obst[0])
                    for key in obstaclehit.keys():
                        if not key.is_super:
                            all_sprites.remove(key)
                            bullets.remove(key)
                            break
                elif not obst[0].destructibility:
                    for key in obstaclehit.keys():
                            all_sprites.remove(key)
                            bullets.remove(key)
                            break


            # for key in obstaclehit.keys():
            #     if not key.is_super:
            #         all_sprites.remove(key)
            #         bullets.remove(key)
            #         break

        obstaclehit1 = pygame.sprite.groupcollide(enemy_bullets, obstacles, True, False)
        if obstaclehit1:
            for obst in obstaclehit1.values():
                if obst[0].destructibility:
                    obst[0].kill()
                    obstacles.remove(obst[0])
                    all_sprites.remove(obst[0])
        obstaclecrash = pygame.sprite.spritecollide(player, obstacles, False)
        if obstaclecrash:
            for key in obstaclecrash:
                if not player.no_walls:
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

        mobhits = pygame.sprite.groupcollide(mobs, bullets, False, False)
        if mobhits:
            for key in mobhits:
                if not mobhits[key][0].is_super:
                    all_sprites.remove(mobhits[key])
                    bullets.remove(mobhits[key])
                enemy_hit.play()
                player.points = player.points + 1
                all_sprites.remove(key)
                mobs.remove(key)
                expl = Explosion(key.rect.centerx, key.rect.centery)
                all_sprites.add(expl)
                n = random.randrange(0, mobs_location.__len__())
                m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1), random.choice([0, 1, 2]))
                all_sprites.add(m)
                mobs.add(m)
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
                if player.is_detected or (not player.is_detected and player.mask):
                    player.points = player.points + 1
                    player_hit.play()
                mobs.remove(key)
                all_sprites.remove(key)
                n = random.randrange(0, mobs_location.__len__())
                m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1), random.choice([0, 1, 2]))
                all_sprites.add(m)
                mobs.add(m)
            if not player.god_mode and (player.is_detected or (not player.is_detected and player.mask)):
                player.lives = player.lives - 1

            if player.lives > 0:

                if not player.autopilot_on and not player.god_mode and not player.destination_on:
                    if mask.__len__() != 0:
                        player.mask = False
                        all_sprites.remove(mask)
                        mask.empty()
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
                if player.destination_on:
                    all_sprites.remove(enemy_bullets)
                    enemy_bullets.empty()
                    player.safe_location = player_coordinates
                    player.is_detected = False
                    player.destination_on = False
                    player.lives = player_lives
                    player.rect.left = player_coordinates.__getitem__(0) * 50
                    player.rect.top = player_coordinates.__getitem__(1) * 50
                    player.direction = 'up'
                    player.image = pygame.transform.scale(player_img1, (50, 50))
                    player.image.set_colorkey(WHITE)
                else:
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
                    if player.is_detected or (not player.is_detected and player.mask):
                        player.lives = player.lives - 1
                    if player.lives > 0:
                        if not player.autopilot_on and not player.destination_on:
                            if mask.__len__() != 0:
                                player.mask = False
                                all_sprites.remove(mask)
                                mask.empty()
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
        draw_text(screen, 'score: ' + str(player.points), 30, WIDTH / 2, 5, RED)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_img_mini)
        draw_icons(screen)
        pygame.display.flip()

    pygame.quit()


main()
