import pygame
import config
from game_state import GameState

from game import Game

pygame.init()

screen=pygame.display.set_mode((config.SCREEN_WIDTH,config.SCREEN_HEIGHT))

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()	#for framerate

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
	clock.tick(20)	#framerate
	game.update()
	pygame.display.flip()