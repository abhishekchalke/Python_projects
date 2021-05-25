import pygame

import game_functions as gf



def run():
	pygame.init()
	screen = pygame.display.set_mode((1200, 600))

	li = []

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				for re in li:
					print('TOP :', re.top)
					print('BOTTOM :', re.bottom)
					print('LEFT :', re.left)
					print('RIGHT :', re.right)
					print('CENTER :', re.center)
					print('CENTER-X :', re.centerx)
					print('CENTER-Y :', re.centery)
					print('X :', re.x)
					print('Y :', re.y)
					print(help(re))


				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					li.append(irect)



		screen.fill((255, 255, 255))
		

		image = pygame.image.load('images/shinchan.jfif')
		srect = screen.get_rect()
		irect = image.get_rect()

		#irect.bottom = srect.bottom
		irect.center = srect.center


		screen.blit(image, irect)
		pygame.display.flip()





#run()



def run2():
	pygame.init()
	screen = pygame.display.set_mode((1200, 600))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.unicode == 'd':
					run()


		screen.fill((230,230,230))
		pygame.display.flip()



run2()


