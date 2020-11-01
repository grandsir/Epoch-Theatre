# Created by GrandSir in 11.07.2020
# This game developed by GrandSir

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pathlib
from Images import *
from Graphics import *
import traceback
import pygame as pg
from Menu import MenuScreen
from Settings import *
from Scenes import Scene

class Game:
    def __init__(self):
        #initializing window
        pg.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT),0,32)
        self.m = MenuScreen(self.screen)

        # Current ScWidget
        self.DialogBox = DialogBox()

        ## refer to self.DialogBox object (ScWidget can be ChoiceBox or DialogBox)
        self.ScWidget = self.DialogBox 
            

        #List Scene folder
        self.scene_file = iter(os.listdir(str(path.joinpath("Scene"))))
        self._scene = next(self.scene_file)
        self.current_scene = str(path.joinpath("Scene", self._scene))
        self.scene = Scene(self.current_scene)
        self.image_dict = self.list_folder(path.joinpath("Characters"))
        self.clock = pg.time.Clock()
        self.running = True


    def list_folder(self, folder_path):
        #creates dictionary from folder
        Folders = sorted(os.listdir(folder_path))
        images = dict()
        for i in Folders:
            Files = sorted(os.listdir(str(folder_path.joinpath(i))))
            for file in Files:
                basename = os.path.basename(str(path.joinpath(file)))
                images[basename[:basename.index(".")]] = pg.image.load(str(path.joinpath(folder_path, i, file))).convert_alpha()

        return images

    def new(self):
        self.run()

    def draw(self):
        ### Clear Screen
        self.info_object = pg.display.Info()
        background_image = pg.image.load(Images["background"])
        background_image_resized = pg.transform.scale(background_image, (info_object.current_w, info_object.current_h))
        self.screen.blit(background_image_resized, (0,0)) 

        ### Draw the game elements
        self.scene.draw(self.screen, self.image_dict)
        self.ScWidget.draw(self.screen)

        ### Finally, update the screen
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                #Go to next event when mouse pressed
                self.scene.update(self.ScWidget)
                if self.scene.error:
                    try:
                        #if a scene ends, pass into the next one.
                        self._scene = next(self.scene_file)
                        self.current_scene = str(path.joinpath("Scene", self._scene))
                        self.scene.update_scene = self.current_scene
                        self.scene.set_error = False

                    except StopIteration:
                        print("oyun bitti")

                    except:
                        log_file = str(path.joinpath("Logs", "logs.txt"))
                        with open(log_file, "r+", encoding="utf-8") as file:
                            #get error from log, and write it to logs.txt 
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            traceback.print_tb(exc_traceback, file=file)
                            traceback.print_exception(exc_type, exc_value, exc_traceback, file=file)
                            #and finally, apologize for error xd
                            file.write("\nTr: Böyle bir hata ile karşılaştığınız için özür dileriz. Sorununuzu çözmek ve başkalarının aynı hatayı yaşamasını önlemek için sizi discord sunucumuza davet ediyoruz.\nEn: We apologize for this error. We welcome you to our discord server to solve your problem and to prevent other people from experiencing the same error.\nhttps://discord.gg/BZ7zfKb")

                        os.system(log_file)
                        self.quit()



    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.info_object = pg.display.Info()

        # FIX: widgets should resize at the resizing window.
        self.ScWidget.resize(self.info_object.current_w, self.info_object.current_h)

    def show_start_screen(self):
        self.m.run()
        pg.mouse.set_visible(True)


    def show_continue_screen(self):
        pass

    def quit(self):
        pg.mixer.quit()
        pg.quit()
        sys.exit()

g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_continue_screen()
