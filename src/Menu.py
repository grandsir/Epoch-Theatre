# Created by GrandSir in 18.07.2020
# This game developed by GrandSir

from Graphics import *
import sys
import json
import random
from pygame.locals import BLEND_RGB_ADD
from Images import *
from Settings import *

class MenuScreen:
    def __init__(self, screen_surface):
        self.particles = []
        pg.init()
        self.screen = screen_surface

        self.clock = pg.time.Clock()
        self.Buttons = dict()

        self.fade = Fade(FULLSCREEN_W, FULLSCREEN_H, 5)

        self.Buttons["newgame"] = Button(Images["newgame_button"], Images["newgame_button_hovered"], (WIDTH/2) - 300, (HEIGHT/2) - 300, self.new_game)

        self.Buttons["load_save"] = Button(Images["continue_button"], Images["continue_hovered"], (WIDTH/2) - 290, (HEIGHT/2) - 100, lambda: self.stackedw.set_current_state("load_save"))

        self.Buttons["fullscreen"] = Button(Images["fullscreen_button"], Images["fullscreen_button_hovered"], (WIDTH/2)-200, (HEIGHT/2), self.set_fullscreen)

        self.Buttons["match_aspect_ratio"] = Button(Images["Match_Aspect_Ratio_button"], Images["Match_Aspect_Ratio_button_hovered"], (WIDTH-400), (HEIGHT/2), self.match_aspect_ratio)

        self.Buttons["windowed"] = Button(Images["newgame_button"], Images["newgame_button_hovered"], 0 , (HEIGHT/2), self.windowed)


        self.all_states = ("mainmenu", "load_save")

        self.stackedw = Stackedwidget(screen_surface, "mainmenu", self.all_states)

        self.stackedw.add_group([self.Buttons["newgame"],self.Buttons["load_save"]], "mainmenu")
        self.stackedw.add_widget((self.Buttons["fullscreen"], self.Buttons["match_aspect_ratio"], self.Buttons["windowed"]), "load_save")

        self.image = pg.image.load(Images["background"]).convert_alpha()
        self.image_resized = pg.transform.scale(self.image, (WIDTH,HEIGHT))

        pg.mouse.set_visible(False)  # hide the cursor



    def windowed(self):
        self.image_resized = pg.transform.scale(self.image, (WIDTH,HEIGHT))
        pg.display.set_mode((WIDTH, HEIGHT))

    def set_fullscreen(self):
        self.image_resized = pg.transform.scale(self.image, (FULLSCREEN_W, FULLSCREEN_H))
        pg.display.set_mode((FULLSCREEN_W, FULLSCREEN_H))
        pg.display.set_mode((0,0), pg.FULLSCREEN)


    def match_aspect_ratio(self):
        self.image_resized = pg.transform.scale(self.image, (FULLSCREEN_W, FULLSCREEN_H))
        pg.display.set_mode((FULLSCREEN_W, FULLSCREEN_H))

    def resize(self):
        pass

    def new_game(self):
        self.menu_state = False
        fade_state = True
        self.fade.start()   
        while fade_state:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
            if not self.fade.update():
                fade_state = False


            self.fade.draw(self.screen)
            self.clock.tick(60)
            pg.display.flip()


    def run(self):
        self.menu_state = True
        while self.menu_state:
            self.dt = self.clock.tick(60) / 1000
            self.resize()
            self.events()
            self.draw()

        

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
               if event.key == pg.K_ESCAPE:
                   self.stackedw.set_current_state("mainmenu")
            if event.type == pg.QUIT:
                self.quit()

            self.stackedw.update(event)


    def draw(self):
        if self.menu_state:
            self.screen.blit(self.image_resized, (0,0))
            self.stackedw.draw()
            self.createparticles()
            pg.display.flip()

        else:
            self.screen.fill((0,0,0))

    def circles(self,radius,color):
        radius = int(radius)
        surf = pg.Surface((radius*2, radius*2))
        pg.draw.circle(surf, color, (radius,radius), radius)
        surf.set_colorkey((0,0,0))
        return surf

    def createparticles(self):
        mx, my = pg.mouse.get_pos()
        self.particles.append([[mx, my], [random.randint(0, 20) / 10 -1, -2], random.randint(2,3)])

        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.15
            pg.draw.circle(self.screen, (255,255,255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            radius = particle[2] * 2
            self.screen.blit(self.circles(radius, (25,25,60)), (int(
                particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)

            if particle[2] <= 0:
                self.particles.remove(particle)

    def quit(self):
        pg.mixer.quit()
        pg.quit()
        sys.exit()




