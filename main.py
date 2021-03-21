import random
import math
import pygame
import time

pygame.init()

# Window
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ahmed's Snake Game")

# Colors
white = (255,255,255)
black = (0,0,0)
teal = (0,128,128)
yellow = (255,204,0)
purple = (128,0,128)

# Snake init
snakeBlock = 10
snakeSpeed = 15

# Init
clock = pygame.time.Clock()

# Outputs text to screen
def text(msg, colour, size, x, y):
	font = pygame.font.Font("arial.ttf", size)
	message = font.render(msg, True, colour)
	window.blit(message, [x, y])

# Grows snake when it eats food
def growSnake(snakeBlock, snakeList):
	for square in snakeList:
		pygame.draw.rect(window, teal, [square[0], square[1], snakeBlock, snakeBlock])

# Gives some small room for error when eating food
def ranging(check ,rang):
	upper = rang + 10
	lower = rang - 10
	current = rang - 10
	while current <= upper:
		if check == current:
			return True
		else:
			current+=1
	return False

# Main Function
def gameLoop():
	gameOver = False
	closeGame = False
	background = black
	score = 0

	posx = int(width/2)
	posy = int(height/2)
	xchange = 0
	ychange = 0
	snakeList = []
	snakeLength = 1
	foodx = int(round(random.randrange(0, width - snakeBlock) / 10.0) * 10.0)
	foody = int(round(random.randrange(0, height - snakeBlock) / 10.0) * 10.0)

	# Main game loop
	while not(gameOver):

		while (closeGame):
			window.fill(background)
			text("Game over! Press Q-Quit or P-Play Again", purple, 25, 60, 200)
			pygame.display.update()
			for event in pygame.event.get():
				if event.key == pygame.K_q:
					gameOver = True
					closeGame = False
				if event.key == pygame.K_p:
					gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameOver = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					xchange = snakeBlock
					ychange = 0
				elif event.key == pygame.K_LEFT:
					xchange = -snakeBlock
					ychange = 0
				elif event.key == pygame.K_UP:
					ychange = -snakeBlock
					xchange = 0
				elif event.key == pygame.K_DOWN:
					ychange = snakeBlock
					xchange = 0
				elif event.key == pygame.K_d:
					if background == black:
						background = white
					else:
						background = black

		if posx >= width or posx < 0 or posy >= height or posy < 0:
			closeGame = True

		posx += xchange
		posy += ychange
		window.fill(background)
		pygame.draw.rect(window, yellow, [foodx, foody, snakeBlock, snakeBlock])

		snakeHead = []
		snakeHead.append(posx)
		snakeHead.append(posy)
		snakeList.append(snakeHead)
		if len(snakeList) > snakeLength:
			del snakeList[0]
		for square in snakeList[:-1]:
			if square == snakeHead:
				closeGame = True
		growSnake(snakeBlock, snakeList)

		text(("Score: " + str(score)), purple, 20, 10, 10)

		pygame.display.update()

		if ranging(posx, foodx) and ranging(posy, foody):
			foodx = round(random.randrange(0, width - snakeBlock))
			foody = round(random.randrange(0, height - snakeBlock))
			snakeLength += 1
			score += 1

		clock.tick(snakeSpeed)

	pygame.quit()
	quit()

gameLoop()