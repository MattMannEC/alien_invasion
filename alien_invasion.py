import sys
import pygame
from settings import Settings

class AlienInvasion:
    #do you always init self in python ?
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        # each element of a game should have it's own surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Active flag for game """
        while True:
            # Listen for keyboard and mouse events
            # get() handles for none
            # event returns an object of events that occured since the last while iteration
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #deletes the old screen and generates a new one taking into account the new events

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()