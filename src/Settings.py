# Created by GrandSir in 23.07.2020
# This game developed by GrandSir

import pygame as pg
import pathlib
import json
pg.init()
info_object = pg.display.Info()

cfg_path = pathlib.Path(__file__).resolve().parent
config_path = str(cfg_path.joinpath("Settings.json"))

with open(config_path, "r", encoding= "utf-8") as dosya:
    config_obj = json.load(dosya)

WIDTH = config_obj["WIDTH"]
HEIGHT = config_obj["HEIGHT"]

FULLSCREEN_W = info_object.current_w
FULLSCREEN_H = info_object.current_h

FPS = config_obj["FPS"]
TITLE = config_obj["TITLE"]

FONT_NAME = config_obj["FONT_NAME"]
OPACITY_VALUE = config_obj["OPACITY_VALUE"]

FADE_OPACITY = config_obj["FADE_OPACITY"]
FADE_TIME = config_obj["FADE_TIME"]
