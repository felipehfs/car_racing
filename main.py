#! /usr/bin/env python3

import pygame, random, datetime

from car import Car

pygame.init()

frame_rate = 60
score = 0

# Colors
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

WIDTH = 400
HEIGHT = 500

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car racing')

all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = HEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = -100

car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(CYAN, 60,80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(BLUE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_comming_cars = pygame.sprite.Group()
all_comming_cars.add(car1)
all_comming_cars.add(car2)
all_comming_cars.add(car3)
all_comming_cars.add(car4)

# song configurations
pygame.mixer.music.load('assets/songs/song_one.mp3')

carryOn = True
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)
while carryOn:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				playerCar.moveRight(10)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		playerCar.moveLeft(5)
	if keys[pygame.K_RIGHT]:
		playerCar.moveRight(5)
	if keys[pygame.K_UP]:
		speed += 0.05
	if keys[pygame.K_DOWN]:
		speed -= 0.05
	# -- Timer ---
	

	score += 1

	# Game logic
	for car in all_comming_cars:
		car.moveForward(speed)
		if car.rect.y > HEIGHT:
			car.changeSpeed(random.randint(50, 100))
			car.repaint(random.choice(colorList))
			car.rect.y = -200
	#Check if there is a car collision
	car_collision_list = pygame.sprite.spritecollide(playerCar, all_comming_cars, False)
	for car in car_collision_list:
		print('Car crash!')
		carryOn = False
		
	all_sprites_list.update()

	#Drawing on screen
	screen.fill(GREEN)
	#Draw the road
	pygame.draw.rect(screen, GREY, [40, 0, 400, HEIGHT])
	# Draw line paiting on the road
	pygame.draw.line(screen, WHITE, [140, 0], [140, HEIGHT], 5)
	# Draw line paiting on the road
	pygame.draw.line(screen, WHITE, [240, 0], [240, HEIGHT], 5)
	# Draw line paiting on the road
	pygame.draw.line(screen, WHITE, [340, 0], [340, HEIGHT], 5)

	# Now let's draw all the sprites in one go.
	all_sprites_list.draw(screen)
	myFont = pygame.font.SysFont('Arial', 30)
	label = myFont.render("Score: {}".format(score), True, WHITE)

	screen.blit(label, [150, 30])
	# Refresh screen
	pygame.display.flip()

	# Number of frame per second e.g.  60 
	clock.tick(frame_rate)
pygame.mixer.music.stop()
pygame.quit()