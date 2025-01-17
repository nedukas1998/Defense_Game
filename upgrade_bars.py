import pygame


class TowerMenu():
    ''' Towers menu on the bottom of the screen. '''

    def __init__(self, game):

        self.main_game = game
        # Loading image of the tower menu.
        self.image = pygame.transform.scale(pygame.image.load(
            'images_final/Towers/Menu_bar/window_3.png').convert_alpha(), (420, 95))
        # Creating rect for the tower menu image.
        self.rect = self.image.get_rect(
            midbottom=(210, self.main_game.rect.bottom))

    def draw(self):
        ''' Drawing the tower menu to the surface. '''
        self.main_game.screen.blit(self.image, self.rect)

    def check_collision(self, mouse_pos):
        ''' Checking collision with specific tower's icon (in tower menu). '''
        if self.main_game.tower1.rect_around_icon.collidepoint(mouse_pos):
            self.main_game.selected_tower = self.main_game._create_tower(
                'Tower1')
        elif self.main_game.tower2.rect_around_icon.collidepoint(mouse_pos):
            self.main_game.selected_tower = self.main_game._create_tower(
                'Tower2')
        elif self.main_game.tower3.rect_around_icon.collidepoint(mouse_pos):
            self.main_game.selected_tower = self.main_game._create_tower(
                'Tower3')
        elif self.main_game.tower4.rect_around_icon.collidepoint(mouse_pos):
            self.main_game.selected_tower = self.main_game._create_tower(
                'Tower4')
