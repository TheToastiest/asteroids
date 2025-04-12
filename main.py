import pygame
import constants

def main():
	pygame.init()
	pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return

if __name__ == "__main__":
    main()
