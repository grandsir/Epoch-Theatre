# Created by GrandSir in 29.07.2020
# This game developed by GrandSir

import json 
import pathlib
path = pathlib.Path(__file__).resolve().parent
json_path = str(path.joinpath("test.json"))

with open(json_path, "r+", encoding= "utf-8") as scfl:
    scene_file = json.load(scfl)

def setbottomtext(emote, character, dialog):
    return '{}({})\n>{}'.format(character, emote, dialog)

event_items = scene_file["main"]["events"][0]
item = event_items["item"]
asd = scene_file[event_items["event_type"]][item]


#output:
"""

megami(horny) 
> OH YEAH

"""
