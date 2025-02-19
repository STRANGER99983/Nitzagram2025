import pygame
from constants import *

class Post:

    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

        font = pygame.font.SysFont('Arial', 24)
        self.username_text = font.render(self.username, True, "black")
        self.location_text = font.render(self.location, True, "black")
        self.description_text = font.render(self.description, True ,"black")


    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def display(self, screen, post):

        screen.blit(post, (POST_X_POS, POST_Y_POS))
        screen.blit(self.username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(self.location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        screen.blit(self.description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
