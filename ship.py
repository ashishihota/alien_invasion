import pygame

class Ship:

    def __init__(self, screen):
        self.screen = screen

        # Load the ship image and get its rectangle(rect)
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx #center of ship and screen_rect
        self.rect.bottom = self.screen_rect.bottom #bottom of the ship and the screen

        # Movement Flag
        self.moving_right = False # adding a right attribute
        self.moving_left = False # adding a left attribute



    def update(self):
        """ Update the ships position based on the movement falg """
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    # Draw the image to the sreen at the given position
    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
