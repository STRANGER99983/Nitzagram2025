import pygame
from constants import *
from helpers import from_text_to_array, center_text

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

    def display(self, screen):

        screen.blit(self.username_text, (USER_NAME_X_POS, USER_NAME_Y_POS))
        screen.blit(self.location_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        screen.blit(self.description_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

class ImagePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (POST_WIDTH, POST_HEIGHT))

    def display(self, screen):
        screen.blit(self.image, (POST_X_POS, POST_Y_POS))
        super().display(screen)


class TextPost(Post):
    def __init__(self, username, location, description, text_content):
        super().__init__(username, location, description)
        self.text_content = text_content

    def display(self, screen, text_color, backround_color):
        text = from_text_to_array(self.text_content)
        pygame.draw.rect(screen, backround_color, (POST_X_POS, POST_Y_POS, POST_X_POS+291, POST_Y_POS+145))

        font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        rendered_text = []
        for sent in text:
            rendered_text.append(font.render(sent, True, text_color))

        for i in range(len(rendered_text)):
            screen.blit(rendered_text[i], center_text(len(rendered_text), rendered_text[i], i+1))

        super().display(screen)



