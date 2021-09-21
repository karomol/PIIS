import pygame
import random
import pygame.freetype
from os import path

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
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's battle!")
clock = pygame.time.Clock()
background = pygame.image.load(path.join('sprite_images', 'ground02.bmp')).convert()
background = pygame.transform.scale(background, (800, 700))
background_rect = background.get_rect()
player_img1 = pygame.image.load(path.join('sprite_images', "pla1.bmp")).convert()
player_img2 = pygame.image.load(path.join('sprite_images', "pla2.bmp")).convert()
player_img3 = pygame.image.load(path.join('sprite_images', "pla3.bmp")).convert()
player_img4 = pygame.image.load(path.join('sprite_images', "pla4.bmp")).convert()
obstacle_img1 = pygame.image.load(path.join('sprite_images', "block_02.bmp")).convert()
obstacle_img2 = pygame.image.load(path.join('sprite_images', "block_08.bmp")).convert()
bullet1_img = pygame.image.load(path.join('sprite_images', "bullet1.png")).convert()
bullet2_img = pygame.image.load(path.join('sprite_images', "bullet2.png")).convert()
bullet3_img = pygame.image.load(path.join('sprite_images', "bullet3.png")).convert()
bullet4_img = pygame.image.load(path.join('sprite_images', "bullet4.png")).convert()
mob_img1 = pygame.image.load(path.join('sprite_images', "v1.bmp")).convert()
mob_img2 = pygame.image.load(path.join('sprite_images', "v2.bmp")).convert()
mob_img3 = pygame.image.load(path.join('sprite_images', "v3.bmp")).convert()
mob_img4 = pygame.image.load(path.join('sprite_images', "v4.bmp")).convert()
back_img = pygame.image.load(path.join('sprite_images', "i_background.jpg")).convert()
back_img = pygame.transform.scale(back_img, (800, 700))
back_img_rect = back_img.get_rect()
panel = pygame.image.load(path.join('sprite_images', "panel.bmp")).convert()
panel = pygame.transform.scale(panel, (WIDTH, 50))
panel_rect = panel.get_rect()
panel_rect.x = 0
panel_rect.y = 0
player_img_mini = pygame.image.load(path.join('sprite_images', "pla1_mini.bmp")).convert()
player_img_mini = pygame.transform.scale(player_img_mini, (25, 25))
player_img_mini.set_colorkey(WHITE)

mobs_location = ((750, 150), (250, 150),
                 (750, 550), (550, 350),
                 (200, 150), (750, 100),
                 (750, 600), (550, 400),
                 (300, 350), (300, 400))
mobs_number = 7
obstacles_number = 25
player_lives = 5


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img1, (50, 50))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.centerx = 0
        self.rect.bottom = HEIGHT
        self.speedx = 0
        self.speedy = 0
        self.direction = 'up'
        self.cooldown = 1000
        self.shottime = -self.cooldown
        self.bulletspeed = 5
        self.speed = 2
        self.points = 0
        self.lives = player_lives

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.speed
            self.direction = 'left'
            self.image = pygame.transform.scale(player_img2, (50, 50))
            self.image.set_colorkey(WHITE)
        elif keystate[pygame.K_RIGHT]:
            self.speedx = self.speed
            self.direction = 'right'
            self.image = pygame.transform.scale(player_img3, (50, 50))
            self.image.set_colorkey(WHITE)
        elif keystate[pygame.K_UP]:
            self.speedy = -self.speed
            self.direction = 'up'
            self.image = pygame.transform.scale(player_img1, (50, 50))
            self.image.set_colorkey(WHITE)
        elif keystate[pygame.K_DOWN]:
            self.speedy = self.speed
            self.direction = 'down'
            self.image = pygame.transform.scale(player_img4, (50, 50))
            self.image.set_colorkey(WHITE)

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


class Mob(pygame.sprite.Sprite):
    def __init__(self, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mob_img3, (50, 50))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.x = x1
        self.rect.y = y1
        self.speedy = 0
        self.speedx = 0
        self.cooldown = 1000
        self.shottime = -self.cooldown
        self.bulletspeed = 2
        self.speed = 1
        self.direction = 'right'
        self.step = 50
        self.locationx = 0
        self.locationy = y1 - self.step
        self.playerdirection = ' '

    def update(self):
        if self.direction == 'right' and self.rect.x < \
                self.locationx + self.step and self.playerdirection != 'vertical':
            self.image = pygame.transform.scale(mob_img3, (50, 50))
            self.image.set_colorkey(WHITE)
            self.rect.x += self.speed
        if self.direction == 'left' and self.rect.x > \
                self.locationx - self.step and self.playerdirection != 'vertical':
            self.image = pygame.transform.scale(mob_img2, (50, 50))
            self.image.set_colorkey(WHITE)
            self.rect.x += -self.speed
        if self.direction == 'up' and self.rect.y < \
                self.locationy + self.step and self.playerdirection != 'horizontal':
            self.image = pygame.transform.scale(mob_img1, (50, 50))
            self.image.set_colorkey(WHITE)
            self.rect.y += -self.speed
        if self.direction == 'down' and self.rect.y > \
                self.locationy - self.step and self.playerdirection != 'horizontal':
            self.image = pygame.transform.scale(mob_img4, (50, 50))
            self.image.set_colorkey(WHITE)
            self.rect.y += self.speed

        if self.rect.x == self.locationx + self.step:
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.x == self.locationx - self.step:
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.y == self.locationy + self.step:
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.y == self.locationy - self.step:
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.top < 50:
            self.rect.top = 50
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.direction = randomconverter(self.direction)
            self.locationx = self.rect.x
            self.locationy = self.rect.y

        if player.rect.centery - 15 <= self.rect.centery <= player.rect.centery + 15:
            if player.rect.x >= self.rect.centerx:
                temp = 0
                for obst in obstacles:
                    if obst.rect.top <= self.rect.centery <= obst.rect.bottom:
                        if player.rect.right > obst.rect.right > self.rect.right:
                            temp = temp + 1
                if temp == 0:
                    self.playerdirection = 'horizontal'
                    self.image = pygame.transform.scale(mob_img3, (50, 50))
                    self.image.set_colorkey(WHITE)
                    self.shoot('right')
            if player.rect.centerx < self.rect.centerx:
                temp = 0
                for obst in obstacles:
                    if obst.rect.top <= self.rect.centery <= obst.rect.bottom:
                        if player.rect.right < obst.rect.right < self.rect.right:
                            temp = temp + 1
                if temp == 0:
                    self.playerdirection = 'horizontal'
                    self.image = pygame.transform.scale(mob_img2, (50, 50))
                    self.image.set_colorkey(WHITE)
                    self.shoot('left')
        else:
            self.playerdirection = ' '

        if player.rect.centerx - 15 <= self.rect.centerx <= player.rect.centerx + 15:
            if player.rect.centery >= self.rect.centery:
                temp = 0
                for obst in obstacles:
                    if obst.rect.left <= self.rect.centerx <= obst.rect.right:
                        if player.rect.bottom > obst.rect.bottom > self.rect.bottom:
                            temp = temp + 1
                if temp == 0:
                    self.playerdirection = 'vertical'
                    self.image = pygame.transform.scale(mob_img4, (50, 50))
                    self.image.set_colorkey(WHITE)
                    self.shoot('down')
            if player.rect.centery < self.rect.centery:
                temp = 0
                for obst in obstacles:
                    if obst.rect.left <= self.rect.centerx <= obst.rect.right:
                        if player.rect.bottom < obst.rect.bottom < self.rect.bottom:
                            temp = temp + 1
                if temp == 0:
                    self.playerdirection = 'vertical'
                    self.image = pygame.transform.scale(mob_img1, (50, 50))
                    self.image.set_colorkey(WHITE)
                    self.shoot('up')

    def shoot(self, direction):
        if pygame.time.get_ticks() >= self.shottime + self.cooldown:
            self.shottime = pygame.time.get_ticks()
            bullet = Bullet(self.rect.top, self.rect.bottom,
                            self.rect.centerx, self.rect.centery, self.rect.right,
                            self.rect.left, direction, self.bulletspeed)
            all_sprites.add(bullet)
            enemy_bullets.add(bullet)


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
        self.rect.x = x
        self.destructibility = d


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

def random_obstacles(number):
    i = 0
    while True and i < number:
        locationx = random.randrange(0, WIDTH-49, 50)
        locationy = random.randrange(50, HEIGHT-49, 50)
        temp = 0
        for obst in obstacles:
            for n in mobs_location:
                if locationx == n.__getitem__(0) and locationy == n.__getitem__(1) :
                    temp = 1
                    break
            if obst.rect.x == locationx and obst.rect.y == locationy or locationx == 0 \
                    and locationy == HEIGHT-50:
                temp = 1
                break
        if temp == 0:
            i = i + 1
            obst = Obstacle(locationx, locationy, True)
            obstacles.add(obst)
            all_sprites.add(obst)




font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y, colour):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 15 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen():
    screen.blit(back_img, back_img_rect)
    draw_text(screen, "Your score: " + str(player.points), 64, WIDTH / 2, HEIGHT / 3, GREEN)
    draw_text(screen, "Remember: arrow keys to move, Space to fire, Escape to pause", 30,
              WIDTH / 2, HEIGHT / 2, RED)
    draw_text(screen, "Press Home to begin", 30, WIDTH / 2, HEIGHT * 3 / 4, BLUE)
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
                if event.key == pygame.K_HOME:
                    return True
                    waiting = False




all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

obstacle = Obstacle(0, 550)
obstacle1 = Obstacle(50, 400)
obstacle2 = Obstacle(100, 400)
obstacle3 = Obstacle(100, 450)
obstacle4 = Obstacle(500, 500)
obstacle5 = Obstacle(50, 100)
obstacle6 = Obstacle(200, 550)
obstacle7 = Obstacle(200, 600)
obstacle8 = Obstacle(150, 450)
obstacle9 = Obstacle(100, 100)
obstacle10 = Obstacle(100, 150)
obstacle11 = Obstacle(0, 250)
obstacle12 = Obstacle(350, 350)
obstacle13 = Obstacle(450, 100)
obstacle14 = Obstacle(350, 200)
obstacle15 = Obstacle(450, 600)
obstacle16 = Obstacle(350, 550)
obstacle17 = Obstacle(350, 500)
obstacle18 = Obstacle(350, 450)
obstacle19 = Obstacle(300, 450)
obstacle20 = Obstacle(50, 350)
obstacle21 = Obstacle(450, 300)
obstacle22 = Obstacle(550, 150)
obstacle23 = Obstacle(550, 100)
obstacle24 = Obstacle(550, 200)
obstacle25 = Obstacle(600, 550)
obstacle26 = Obstacle(400, 450)
obstacle27 = Obstacle(600, 100)
obstacle28 = Obstacle(350, 250)
obstacle30 = Obstacle(350, 400)
obstacle31 = Obstacle(550, 450)
obstacle32 = Obstacle(650, 550)
obstacle33 = Obstacle(100, 300)
obstacle34 = Obstacle(150, 300)
obstacle35 = Obstacle(200, 350)
obstacle36 = Obstacle(100, 350)
obstacle37 = Obstacle(150, 200)
obstacle38 = Obstacle(200, 200)
obstacle39 = Obstacle(250, 100)
obstacle40 = Obstacle(650, 100)
obstacle41 = Obstacle(650, 200)
obstacle42 = Obstacle(700, 100)
obstacle43 = Obstacle(700, 200)
obstacle44 = Obstacle(750, 200)
obstacle45 = Obstacle(700, 350)
obstacle46 = Obstacle(650, 400)
obstacle47 = Obstacle(700, 400)
obstacle48 = Obstacle(750, 500)
obstacle49 = Obstacle(350, 300)
obstacle50 = Obstacle(450, 50)
obstacle51 = Obstacle(650, 250)
obstacle52 = Obstacle(750, 700)

obstacles.add(obstacle, obstacle1, obstacle2, obstacle3, obstacle4)
obstacles.add(obstacle5, obstacle6, obstacle7, obstacle8, obstacle9, obstacle10, obstacle11)
obstacles.add(obstacle12, obstacle13, obstacle14, obstacle15, obstacle16, obstacle17)
obstacles.add(obstacle18, obstacle19, obstacle20, obstacle21)
obstacles.add(obstacle22, obstacle23, obstacle24, obstacle25, obstacle26, obstacle27)
obstacles.add(obstacle28, obstacle30, obstacle31, obstacle32)
obstacles.add(obstacle32, obstacle33, obstacle34, obstacle35)
obstacles.add(obstacle36, obstacle37, obstacle38, obstacle39)
obstacles.add(obstacle40, obstacle41, obstacle42, obstacle43)
obstacles.add(obstacle44, obstacle45, obstacle46, obstacle47, obstacle48, obstacle49, obstacle50)
obstacles.add(obstacle51, obstacle52)

all_sprites.add(obstacle, obstacle1, obstacle2, obstacle3, obstacle4)
all_sprites.add(obstacle5, obstacle6, obstacle7, obstacle8, obstacle9, obstacle10, obstacle11)
all_sprites.add(obstacle12, obstacle13, obstacle14, obstacle15, obstacle16, obstacle17)
all_sprites.add(obstacle18, obstacle19, obstacle20, obstacle21)
all_sprites.add(obstacle22, obstacle23, obstacle24, obstacle25, obstacle26, obstacle27)
all_sprites.add(obstacle28, obstacle30, obstacle31, obstacle32)
all_sprites.add(obstacle32, obstacle33, obstacle34, obstacle35)
all_sprites.add(obstacle36, obstacle37, obstacle38, obstacle39)
all_sprites.add(obstacle40, obstacle41, obstacle42, obstacle43)
all_sprites.add(obstacle44, obstacle45, obstacle46, obstacle47, obstacle48, obstacle49, obstacle50)
all_sprites.add(obstacle51, obstacle52)
player = Player()
all_sprites.add(player)
random_obstacles(obstacles_number)

for i in range(mobs_number):
    n = random.randrange(0, mobs_location.__len__())
    m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1))
    all_sprites.add(m)
    mobs.add(m)

game_over = False
running = True
while running:
    screen.fill(BLACK)
    all_sprites.draw(screen)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                waiting = True
                while waiting:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting = False
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                waiting = False

    all_sprites.update()

    bullethit = pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)
    obstaclehit = pygame.sprite.groupcollide(bullets, obstacles, True, False)
    if obstaclehit:
        for obst in obstaclehit.values():
            if obst[0].destructibility:
                obst[0].kill()
                obstacles.remove(obst[0])
                all_sprites.remove(obst[0])

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
                    if key.direction == 'left':
                        key.direction = randomconverter(key.direction)
                        key.rect.x = key.rect.x + key.rect.size[0] - (key.rect.right - en.rect.right)
                        key.locationx = key.rect.x
                        key.locationy = key.rect.y
                    elif key.direction == 'right':
                        key.direction = randomconverter(key.direction)
                        key.rect.x = key.rect.x - key.rect.size[0] - (key.rect.left - en.rect.left)
                        key.locationx = key.rect.x
                        key.locationy = key.rect.y
                    elif key.direction == 'up':
                        key.direction = randomconverter(key.direction)
                        key.rect.y = key.rect.y + key.rect.size[1] - (key.rect.bottom - en.rect.bottom)
                        key.locationx = key.rect.x
                        key.locationy = key.rect.y
                    elif key.direction == 'down':
                        key.direction = randomconverter(key.direction)
                        key.rect.y = key.rect.y - key.rect.size[1] - (key.rect.top - en.rect.top)
                        key.locationx = key.rect.x
                        key.locationy = key.rect.y
                    break
                break
            break

    mobhits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    if mobhits:
        player.points = player.points + 1

    for hit in mobhits:
        n = random.randrange(0, mobs_location.__len__())
        m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1))
        all_sprites.add(m)
        mobs.add(m)

    playerhits = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_rect_ratio(0.9))
    for p in playerhits:
        if playerhits:
            if player.lives > 1:
                player.lives = player.lives - 1
                player.rect.x = 0
                player.rect.y = HEIGHT
                player.direction = 'up'
                player.image = pygame.transform.scale(player_img1, (50, 50))
                player.image.set_colorkey(WHITE)
                break
            else:
                game_over = True
                if not show_go_screen():
                    running = False
                game_over = False
                all_sprites.remove(enemy_bullets, bullets, mobs)
                mobs.empty()
                enemy_bullets.empty()
                bullets.empty()
                clock.tick(FPS)
                player.rect.x = 0
                player.rect.y = HEIGHT
                player.points = 0
                player.lives = player_lives
                for obst in obstacles:
                    if obst.destructibility:
                        obstacles.remove(obst)
                for obst in all_sprites:
                    try:
                        if obst.destructibility:
                            all_sprites.remove(obst)
                    except:
                        continue
                random_obstacles(obstacles_number)
                player.direction = 'up'
                player.image = pygame.transform.scale(player_img1, (50, 50))
                player.image.set_colorkey(WHITE)
                for i in range(mobs_number):
                    n = random.randrange(0, mobs_location.__len__())
                    m = Mob(mobs_location[n].__getitem__(0), mobs_location[n].__getitem__(1))
                    all_sprites.add(m)
                    mobs.add(m)
                break



    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    screen.blit(panel, panel_rect)
    draw_text(screen, 'score: ' + str(player.points), 30, WIDTH / 2, 5, RED)
    draw_lives(screen, WIDTH-100, 5, player.lives, player_img_mini)
    pygame.display.flip()

pygame.quit()
