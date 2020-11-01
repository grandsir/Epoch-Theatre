# Created by GrandSir in 27.07.2020
# This game developed by GrandSir

__import__("os").environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from time import (sleep, time)
from Images import *
from Settings import *

class Stackedwidget(object):
    def __init__(self, surface, currstate, state_scopes):
        self.surface = surface
        self.state_scopes = {state:[] for state in state_scopes}
        self.currstate = currstate # mainmenu ex: mainmenu at start

    def check_state(self, state):
        assert state in self.state_scopes, f"'{state}' doesn't exists."

    def add_widget(self, widget, state):
        self.check_state(state)
        if isinstance(widget, tuple):
            for i in widget:
                self.state_scopes[state].append(i)
        else:
            self.state_scopes[state].append(widget)

    def add_group(self, group, state):
        self.check_state(state)
        for widget in group:
            self.state_scopes[state].append(widget)

    def set_current_state(self, state):
        self.check_state(state)
        self.currstate = state

    def update(self, event):
        for widget in self.state_scopes[self.currstate]:
            widget.handle_event(event)

    def draw(self):
        for widget in self.state_scopes[self.currstate]:
            widget.draw(self.surface)

class Button(object):
    def __init__(self, image, image_hovered, x, y, command= None):
        self.image_normal = pg.image.load(image).convert_alpha()
        self.image_hovered = pg.image.load(image_hovered).convert_alpha()
        self.image = self.image_normal
        self.image_resized = self.image
        self.resized = False
        self.rect = self.image.get_rect(topleft = (x, y))

        self.command = command


    def resize(self, position: tuple, resize_value: tuple):
        self.image_resized = pg.transform.scale(self.image, resize_value)
        self.rect = self.image_resized.get_rect(topleft = position)
        self.resized = True


    def draw(self, surface):
        if self.resized:
            surface.blit(self.image_resized, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def handle_event(self, event):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.image = self.image_hovered
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.command:
                    self.command()
        else:
            self.image = self.image_normal


class DialogBox(pg.sprite.Sprite):
    def __init__(self, title = "", text = ""):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(Images["DialogBoxImage"]).convert_alpha()
        self._title = title 
        self._text  = text

    def _blit_text(self, surface, text, pos, font: "Arial", color=pg.Color('black')):
        
        pass

    def resize(self, x,y):
        self.rect = self.image.get_rect(topleft = (int(x/6), int(y/1.4)-25))
        self.image = pg.transform.scale(self.image, (int(x/1.5), int(y/3.5)))
        
    def draw(self, screen_surface):

        screen_surface.blit(self.image, self.rect)

    def set_text(self, title, text):
        self._title = title
        self._text  = text



class Fade(object):
    def __init__(self, width, height, fade_time):
        self.fade_time = fade_time
        self.width , self.height = width, height
        self.surface = pg.Surface((width, height)) 
        self.surface.fill((0,0,0))       
        self.opacity = 0

    def start(self):
        self.last_update = time()

    def draw(self, screen):
        screen.blit(self.surface, (0,0))

    def update(self):
        self.opacity += FADE_OPACITY
        state_time = time() - self.last_update
        if state_time >= self.fade_time:
            self.last_update = time() - state_time

            return False
            

        
        alpha = self.opacity + (self.opacity * (state_time / self.fade_time))
        self.surface.set_alpha(alpha)


        return True




