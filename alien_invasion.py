import sys

import pygame

class AlienInvasion:
    #do you always init self in python ?
    def __init__(self):

        pygame.init()
        # each element of a game should have it's own surface (ex ship, alien, star)
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Active flag for game """
        while True:
            # Listen for keyboard and mouse events
            # get() handles for none
            # event returns an object of events that occured since the last while iteration
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                self.screen.fill(self.bg_color)

            #deletes the old screen and generates a new one taking into account the new events
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()