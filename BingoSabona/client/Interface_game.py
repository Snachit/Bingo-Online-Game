import pygame
from pygame.locals import *
import subprocess
from pygame import mixer
from network import Network
pygame.init()

clock = pygame.time.Clock()
fps = 60


screen_width = 1500
screen_height = 800



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Bingo Sabona')



#define font
font = pygame.font.SysFont('Bauhaus 93', 230)
font_score = pygame.font.SysFont('Bauhaus 93', 30)


#global variable
tile_size = 50
game_over = 0
level = 1
score1 = 0
score2 = 0


#define colours
white = (255, 255, 255)
red = (255, 0, 0)


# load images
bg_img = pygame.image.load('img/gameInter.png')
stationary_img = pygame.image.load('hero/mario1.png')  # Load your stationary image
stationary_img = pygame.transform.scale(stationary_img, (23, 46))
stationary_imgR = pygame.transform.flip(stationary_img, True, False)
stationary_imgR = pygame.transform.scale(stationary_imgR, (23, 46))
# fire = [pygame.image.load("fire/1.png"), pygame.image.load("fire/2.png"),pygame.image.load("fire/3.png"),pygame.image.load("fire/4.png"),pygame.image.load("fire/6.png")]

restart_img = pygame.image.load('img/restart_btn.png')


# Initialize Pygame mixer
pygame.mixer.init()

coin_sound = pygame.mixer.Sound("img/coin.wav")



# Set the volume of the sound
coin_sound.set_volume(0.5)




# def draw_grid():
#     for line in range(0, 30):
#         pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
     

#function to reset level
def reset_level(level):
    player.reset(100, screen_height - 130)
    #hna ila mat yrje3 lblasa lwla 
    player2.reset(100, screen_height - 130)
    enemies.empty()
    lava_group.empty()
    platform_group.empty()
    chook_group.empty()
    door_group.empty()
    if level == 1:
            world_data = [
                [1, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1], 
                [1, 10, 5, 9, 0, 0, 0, 2, 2, 0, 0, 0, 12, 0, 9, 6, 9, 0, 0, 0, 0, 9, 4, 9, 9, 4, 0, 0, 10, 0, 1], 
                [1, 2, 2, 2, 0, 0, 7, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 9, 0, 7, 2, 2, 2, 2, 2, 2, 13, 2, 2, 1], 
                [1, 9, 0, 0, 0, 0, 1, 0, 9, 0, 9, 0, 1, 0, 0, 0, 0, 2, 2, 0, 9, 1, 1, 0, 0, 0, 0, 9, 9, 0, 1], 
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 7, 0, 0, 0, 0, 0, 0, 13, 1, 1, 0, 0, 0, 0, 2, 2, 0, 1], 
                [1, 13, 0, 2, 9, 4, 9, 0, 0, 0, 9, 0, 1, 1, 0, 0, 0, 0, 9, 0, 9, 1, 1, 9, 0, 0, 9, 0, 0, 0, 1], 
                [1, 9, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 9, 4, 9, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 7, 1], 
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 1, 0, 13, 0, 0, 0, 0, 9, 0, 0, 0, 0, 1], 
                [1, 9, 0, 0, 9, 5, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], 
                [1, 0, 0, 0, 2, 2, 2, 7, 0, 0, 2, 0, 0, 9, 0, 0, 9, 0, 1, 13, 0, 9, 12, 0, 0, 0, 0, 0, 0, 0, 1], 
                [1, 0, 9, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 2, 9, 0, 2, 0, 9, 7, 7, 0, 1], 
                [1, 13, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 2, 1, 0, 0, 1], 
                [1, 0, 0, 0, 0, 9, 0, 1, 0, 0, 1, 0, 9, 0, 12, 0, 9, 0, 0, 9, 0, 0, 0, 0, 9, 7, 1, 1, 9, 0, 1], 
                [1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 1, 0, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1], 
                [1, 0, 0, 0, 5, 0, 9, 1, 11, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 1, 1, 1, 1, 8, 0, 1], 
                [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1]
                ]


    if level == 2 :
            world_data = [
                [1, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1], 
                [1, 10, 5, 9, 0, 0, 0, 2, 2, 0, 0, 0, 12, 0, 9, 6, 9, 0, 0, 0, 0, 9, 4, 9, 9, 4, 0, 0, 10, 0, 1], 
                [1, 2, 2, 2, 0, 0, 7, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 9, 0, 7, 2, 2, 2, 2, 2, 2, 13, 2, 2, 1], 
                [1, 9, 0, 0, 0, 0, 1, 0, 9, 0, 9, 0, 1, 0, 0, 0, 0, 2, 2, 0, 9, 1, 1, 0, 0, 0, 0, 9, 9, 0, 1], 
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 7, 0, 0, 0, 0, 0, 0, 13, 1, 1, 0, 0, 0, 0, 2, 2, 0, 1], 
                [1, 13, 0, 2, 9, 4, 9, 0, 0, 0, 9, 0, 1, 1, 0, 0, 0, 0, 9, 0, 9, 1, 1, 9, 0, 0, 9, 0, 0, 0, 1], 
                [1, 9, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 9, 4, 9, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 7, 1], 
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 1, 0, 13, 0, 0, 0, 0, 9, 0, 0, 0, 0, 1], 
                [1, 9, 0, 0, 9, 5, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], 
                [1, 0, 0, 0, 2, 2, 2, 7, 0, 0, 2, 0, 0, 9, 0, 0, 9, 0, 1, 13, 0, 9, 12, 0, 0, 0, 0, 0, 0, 0, 1], 
                [1, 0, 9, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 2, 9, 0, 2, 0, 9, 7, 7, 0, 1], 
                [1, 13, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 2, 1, 0, 0, 1], 
                [1, 0, 0, 0, 0, 9, 0, 1, 0, 0, 1, 0, 9, 0, 12, 0, 9, 0, 0, 9, 0, 0, 0, 0, 9, 7, 1, 1, 9, 0, 1], 
                [1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 1, 0, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1], 
                [1, 0, 0, 0, 5, 0, 9, 1, 11, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 1, 1, 1, 1, 8, 0, 1], 
                [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1]
                ]
	

    world = World(world_data)
    return world

# def waiting ():
#         screen.fill((0,0,0))
        
#         draw_text('Waiting for other player', font, red, (screen_width // 2) - 500, screen_height // 2 - 100)
    

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False


	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True


		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action





class Player():
    def __init__(self, x, y):
        self.reset(x, y)
    def move(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and not self.jumped and not self.in_air:
            self.vel_y = -15
            self.jumped = True

        if not key[pygame.K_SPACE]:
            self.jumped = False

        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1

        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1

        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = stationary_img
            elif self.direction == -1:
                self.image = stationary_imgR

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            elif self.direction == -1:
                self.image = self.images_left[self.index]

        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        self.in_air = True
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False

        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                    self.vel_y = 0
                    dy = platform.rect.bottom - self.rect.top
                elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                    self.rect.bottom = platform.rect.top - 1
                    self.in_air = False
                    dy = 0
                if platform.move_x != 0:
                    self.rect.x += platform.move_direction

        self.rect.x += dx
        self.rect.y += dy
    def update(self, game_over):

        if game_over == 0:
            
            # check for collision with enemies
            if pygame.sprite.spritecollide(self, enemies, False):
                game_over = -1

            # check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1

            # check for collision with chook
            if pygame.sprite.spritecollide(self, chook_group, False):
                game_over = -1

            # check for collision with door
            if pygame.sprite.spritecollide(self, door_group, False):
                game_over = 1

            # check for collision with fake door
            if pygame.sprite.spritecollide(self, doorFake_group, False):
                self.reset(400, 350)

            # check for collision with water
            if pygame.sprite.spritecollide(self, water_group, False):
                game_over = -1

			

        # elif game_over == -1:
        #     self.image = self.dead_image
        #     draw_text('GAME OVER!', font, red, (screen_width // 2  ) - 500, screen_height // 2 -100)

        #     if self.rect.y > 0:
        #         self.rect.y -= 5

        
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over
    def draw(self):
        # draw player onto screen
        screen.blit(self.image, self.rect)
        
    def reset(self, x , y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0, 3):
            img_right = pygame.image.load(f'hero/mario1_move{num}.png')
            img_right = pygame.transform.scale(img_right, (23, 46))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('img/rip.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True





class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dirt_img = pygame.image.load('img/grass.png')
        grass_img = pygame.image.load('img/land.png')

        row_count = 0

        for row in data:
            col_count = 0

            for tile in row:

                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile_data = (img, img_rect)
                    self.tile_list.append(tile_data)

                elif tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile_data = (img, img_rect)
                    self.tile_list.append(tile_data)

                elif tile == 3:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)

                elif tile == 4:
                    en = Enemy(col_count * tile_size, row_count * tile_size , pygame.image.load('img/enemy.png'))
                    enemies.add(en)

                elif tile == 5:
                    en1 = Enemy(col_count * tile_size, row_count * tile_size , pygame.image.load('img/enemy1.png'))
                    enemies.add(en1)

                elif tile == 6:
                    en2 = Enemy(col_count * tile_size, row_count * tile_size , pygame.image.load('img/enemy2.png'))
                    enemies.add(en2)

                elif tile == 7:
                    chook = Chook(col_count * tile_size, row_count * tile_size )
                    chook_group.add(chook)

                elif tile == 8:
                    door = Door(col_count * tile_size , row_count * tile_size - 50 )
                    door_group.add(door)

                elif tile == 9:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)

                elif tile == 10:
                    door1 = DoorFake(col_count * tile_size , row_count * tile_size - 50 )
                    doorFake_group.add(door1)

                elif tile == 11:
                    water = Water(col_count * tile_size , row_count * tile_size - 200 )
                    water_group.add(water)
                elif tile == 12:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    platform_group.add(platform)
                elif tile == 13:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)
                col_count += 1
            row_count += 1

    def draw(self):

        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

class Enemy(pygame.sprite.Sprite):
     
	def __init__(self, x, y, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1




class Lava(pygame.sprite.Sprite):
     
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/fire.png")
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, move_x, move_y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/land.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_counter = 0
		self.move_direction = 1
		self.move_x = move_x
		self.move_y = move_y


	def update(self):
		self.rect.x += self.move_direction * self.move_x
		self.rect.y += self.move_direction * self.move_y
		self.move_counter += 1
		if abs(self.move_counter) > 50:
			self.move_direction *= -1
			self.move_counter *= -1





class Chook(pygame.sprite.Sprite):
     
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/chook.png")
		self.image = pygame.transform.scale(img, (tile_size, tile_size))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y




class Water(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/water.png")
		self.image = pygame.transform.scale(img, (tile_size * 2 , tile_size * 6))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
          
class Coin(pygame.sprite.Sprite):
     
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/coin.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
          



class Door(pygame.sprite.Sprite):
     
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/door.png")
		self.image = pygame.transform.scale(img, (tile_size * 2, tile_size * 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
          



class DoorFake(pygame.sprite.Sprite):
     
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load("img/door.png")
		self.image = pygame.transform.scale(img, (tile_size * 2, tile_size * 2))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y





if level == 1 :
    world_data = [
                [1, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1], 
                [1, 10, 5, 9, 0, 0, 0, 2, 2, 0, 0, 0, 12, 0, 9, 6, 9, 0, 0, 0, 0, 9, 4, 9, 9, 4, 0, 0, 10, 0, 1], 
                [1, 2, 2, 2, 0, 0, 7, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 9, 0, 7, 2, 2, 2, 2, 2, 2, 13, 2, 2, 1], 
                [1, 9, 0, 0, 0, 0, 1, 0, 9, 0, 9, 0, 1, 0, 0, 0, 0, 2, 2, 0, 9, 1, 1, 0, 0, 0, 0, 9, 9, 0, 1], 
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 7, 0, 0, 0, 0, 0, 0, 13, 1, 1, 0, 0, 0, 0, 2, 2, 0, 1], 
                [1, 13, 0, 2, 9, 4, 9, 0, 0, 0, 9, 0, 1, 1, 0, 0, 0, 0, 9, 0, 9, 1, 1, 9, 0, 0, 9, 0, 0, 0, 1], 
                [1, 9, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 9, 4, 9, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 7, 1], 
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 1, 0, 13, 0, 0, 0, 0, 9, 0, 0, 0, 0, 1], 
                [1, 9, 0, 0, 9, 5, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], 
                [1, 0, 0, 0, 2, 2, 2, 7, 0, 0, 2, 0, 0, 9, 0, 0, 9, 0, 1, 13, 0, 9, 12, 0, 0, 0, 0, 0, 0, 0, 1], 
                [1, 0, 9, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 2, 9, 0, 2, 0, 9, 7, 7, 0, 1], 
                [1, 13, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 2, 1, 0, 0, 1], 
                [1, 0, 0, 0, 0, 9, 0, 1, 0, 0, 1, 0, 9, 0, 12, 0, 9, 0, 0, 9, 0, 0, 0, 0, 9, 7, 1, 1, 9, 0, 1], 
                [1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 1, 0, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1], 
                [1, 0, 0, 0, 5, 0, 9, 1, 11, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 1, 1, 1, 1, 8, 0, 1], 
                [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1]
                ]

if level == 2 :
    	world_data = [
                [1, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 1], 
                [1, 10, 5, 9, 0, 0, 0, 2, 2, 0, 0, 0, 12, 0, 9, 6, 9, 0, 0, 0, 0, 9, 4, 9, 9, 4, 0, 0, 10, 0, 1], 
                [1, 2, 2, 2, 0, 0, 7, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 9, 0, 7, 2, 2, 2, 2, 2, 2, 13, 2, 2, 1], 
                [1, 9, 0, 0, 0, 0, 1, 0, 9, 0, 9, 0, 1, 0, 0, 0, 0, 2, 2, 0, 9, 1, 1, 0, 0, 0, 0, 9, 9, 0, 1], 
                [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 1, 7, 0, 0, 0, 0, 0, 0, 13, 1, 1, 0, 0, 0, 0, 2, 2, 0, 1], 
                [1, 13, 0, 2, 9, 4, 9, 0, 0, 0, 9, 0, 1, 1, 0, 0, 0, 0, 9, 0, 9, 1, 1, 9, 0, 0, 9, 0, 0, 0, 1], 
                [1, 9, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 9, 4, 9, 0, 0, 0, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 0, 7, 1], 
                [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 2, 2, 0, 0, 0, 1, 0, 13, 0, 0, 0, 0, 9, 0, 0, 0, 0, 1], 
                [1, 9, 0, 0, 9, 5, 9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 1, 9, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 1], 
                [1, 0, 0, 0, 2, 2, 2, 7, 0, 0, 2, 0, 0, 9, 0, 0, 9, 0, 1, 13, 0, 9, 12, 0, 0, 0, 0, 0, 0, 0, 1], 
                [1, 0, 9, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 2, 1, 0, 0, 2, 9, 0, 2, 0, 9, 7, 7, 0, 1], 
                [1, 13, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 2, 1, 0, 0, 1], 
                [1, 0, 0, 0, 0, 9, 0, 1, 0, 0, 1, 0, 9, 0, 12, 0, 9, 0, 0, 9, 0, 0, 0, 0, 9, 7, 1, 1, 9, 0, 1], 
                [1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 1, 0, 12, 0, 0, 0, 12, 0, 0, 12, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1], 
                [1, 0, 0, 0, 5, 0, 9, 1, 11, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 1, 1, 1, 1, 8, 0, 1], 
                [1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1]
                ]

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


n = Network()
startPos = read_pos(n.getPos())
player = Player(120,704)
player2 = Player(120,704)


enemies = pygame.sprite.Group()

lava_group = pygame.sprite.Group()

chook_group = pygame.sprite.Group()

water_group = pygame.sprite.Group()

coin_group = pygame.sprite.Group()

platform_group = pygame.sprite.Group()

door_group = pygame.sprite.Group()

doorFake_group = pygame.sprite.Group()

world = World(world_data)

restart_button = Button(screen_width // 2 - 100, screen_height // 2 + 100, restart_img)


#create dummy coin for showing the score
score_coin = Coin(725 , tile_size // 2)
coin_group.add(score_coin)

def redrawWindow(screen, coin_group, enemies,  lava_group, chook_group, world, platform_group, water_group, door_group, doorFake_group, restart_button, player, player2, game_over, font, font_score, white,score1, red, screen_width, screen_height):
    # if :
    #     screen.fill((0, 0, 0))
    #     draw_text('waiting for other players ', font, red, (screen_width // 2) - 500, screen_height // 2 - 100)



    if game_over == 0:
            screen.blit(bg_img, (0, 0))

            world.draw()
            player.draw()
            player2.draw()
            coin_group.draw(screen)
            lava_group.draw(screen)
            chook_group.draw(screen)
            platform_group.draw(screen)
            water_group.draw(screen)
            door_group.draw(screen)
            doorFake_group.draw(screen)
            enemies.draw(screen)
            draw_text('X '+ str(score1), font_score, white, 750, 18)

    if game_over == -1:
        screen.fill((0,0,0))
        
        draw_text('GAME OVER!', font, red, (screen_width // 2) - 500, screen_height // 2 - 100)
    
        restart_button.draw()


    pygame.display.update()

run = True

while run:
    clock.tick(fps)
    
    
    p2Pos = read_pos(n.send(make_pos((player.rect.x, player.rect.y))))
    player2.rect.x = p2Pos[0]
    player2.rect.y = p2Pos[1]
    # draw_grid() 
    if game_over == 0:
        enemies.update()
        platform_group.update()

        if pygame.sprite.spritecollide(player, coin_group, True):
                score1 += 1
                coin_sound.play()

        #hna bax ila player2 dreb dok lcoin
        if pygame.sprite.spritecollide(player2, coin_group, True):
                score2 += 1
                coin_sound.play()


    player.move()
    game_over = player.update(game_over)


    # #if player has died
    # if game_over == -1:
        
    #     if restart_button.draw():
    #         player.reset(100, screen_height - 130)
    #         #hna bach ila mat lplayer tani
    #         player2.reset(100, screen_height - 130)
    #         world_data = []
    #         world = reset_level(level)
    #         game_over = 0
    #         score = 0


    if game_over == 1:
        level += 1
        world_data = []
        world = reset_level(level)
        game_over = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == -1:
            if restart_button.draw():
                player.reset(100, 704)
                #hna bach ila mat lplayer tani
                player2.reset(100, 704)
                world_data = []
                world = reset_level(level)
                game_over = 0
                score1 = 0
                score2 = 0


    redrawWindow(screen, coin_group, enemies,  lava_group, chook_group, world, platform_group, water_group, door_group, doorFake_group, restart_button, player, player2, game_over, font, font_score, white,score1, red, screen_width, screen_height)

pygame.quit()