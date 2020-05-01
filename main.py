import pygame
import config
from game_state import GameState

from game import Game

pygame.init()

screen=pygame.display.set_mode((600,400))

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()	#for framerate

game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
	clock.tick(1)	#framerate
	game.update()
	pygame.display.flip()