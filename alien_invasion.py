import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    #do you always init self in python ?
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        # each element of a game should have it's own surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Active flag for game """
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()


    def check_events(self):
        # Listen for keyboard and mouse events
        # get() handles for none
        # event returns an object of events that occured since the last while iteration
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:   
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    





    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()