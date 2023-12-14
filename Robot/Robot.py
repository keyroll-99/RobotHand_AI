from typing import Tuple

import pygame


class Robot:
    surface: pygame.Surface
    body: pygame.Surface
    upperHand: pygame.Surface
    lowerHand: pygame.Surface
    upperHandReact: Tuple[int, int] | pygame.Rect
    lowerHandReact: Tuple[int, int] | pygame.Rect

    ORIGINAL_UPPER_HAND_SURFACE = pygame.Surface
    ORIGINAL_LOWER_HAND_SURFACE = pygame.Surface
    UPPER_HAND_ORIGINAL_POSITION: Tuple[int, int]
    LOWER_HAND_ORIGINAL_POSITION: Tuple[int, int]

    def __init__(self, screen: pygame.Surface):
        self.surface = screen
        self.body = pygame.image.load("./Assets/Body.png")
        self.ORIGINAL_UPPER_HAND_SURFACE = pygame.image.load("./Assets/UpperHand.png")
        self.ORIGINAL_LOWER_HAND_SURFACE = pygame.image.load("./Assets/LowerHand.png")

        self.upperHand = pygame.transform.rotate(self.ORIGINAL_UPPER_HAND_SURFACE, 0)
        self.lowerHand = pygame.transform.rotate(self.ORIGINAL_LOWER_HAND_SURFACE, 0)

        self.UPPER_HAND_ORIGINAL_POSITION = (self.body.get_width(), 200)
        self.LOWER_HAND_ORIGINAL_POSITION = (self.body.get_width() + self.upperHand.get_width(), 200)
        self.upperHandReact = self.UPPER_HAND_ORIGINAL_POSITION
        self.lowerHandReact = self.LOWER_HAND_ORIGINAL_POSITION

    def draw(self):
        self.surface.blit(self.body, (0, 50))
        self.surface.blit(self.upperHand, self.upperHandReact)
        self.surface.blit(self.lowerHand, self.lowerHandReact)

    #
    def rotate_upper_hand(self, angle):
        pivot = self.UPPER_HAND_ORIGINAL_POSITION
        rotated_image = pygame.transform.rotate(self.ORIGINAL_UPPER_HAND_SURFACE, angle)
        react = rotated_image.get_rect(center=pivot)

        self.upperHandReact = react
        self.upperHand = rotated_image
