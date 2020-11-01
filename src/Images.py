# Created by GrandSir in 16.07.2020
# This game developed by GrandSir

import pathlib

path = pathlib.Path(__file__).resolve().parent
Images = dict()

gui_path = path.joinpath("Gui")
button_path= path.joinpath(gui_path, "Buttons")
background_path = path.joinpath("Background")

Images["newgame_button"] = str(path.joinpath(button_path, "newgame_button.png"))
Images["newgame_button_hovered"] = str(path.joinpath(button_path, "newgame_button_hovered.png"))

Images["continue_button"] = str(path.joinpath(button_path, "Continue_button.png"))
Images["continue_hovered"] = str(path.joinpath(button_path, "Continue_button_hovered.png"))

Images["fullscreen_button"] = str(path.joinpath(button_path, "fullscreen_button.png"))
Images["fullscreen_button_hovered"] = str(path.joinpath(button_path, "fullscreen_button_hovered.png"))

Images["Match_Aspect_Ratio_button"] = str(path.joinpath(button_path, "Match_Aspect_Ratio.png"))
Images["Match_Aspect_Ratio_button_hovered"] = str(path.joinpath(button_path, "Match_Aspect_Ratio_hovered.png"))

Images["background"] = str(path.joinpath(background_path, "background.jpg"))

Images["DialogBoxImage"] = str(path.joinpath(gui_path, "DialogBox.png"))
