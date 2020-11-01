# Created by GrandSir in 27.07.2020
# This game developed by GrandSir

import pathlib
import json
import pygame as pg
from Settings import *
class Scene(object):
	def __init__(self, file):
		with open(file, "r+", encoding="utf-8") as scfile:
			self.scene_file = json.load(scfile)
		self.character_image = ""
		self.eventqueue = iter(self.scene_file["main"]["events"])
		self.current_event = next(self.eventqueue)
		self._event_type = self.current_event["event_type"]
		self.event_type = self.scene_file[self._event_type]
		self.current = self.event_type[self.current_event["item"]]


	@property
	def set_error(self):
		return self.error

	@set_error.setter
	def set_error(self, value: bool):
		self.error = value

	@property
	def update_scene(self):
		return self.scene_file

	@update_scene.setter
	def update_scene(self, file):
		with open(file, "r+", encoding= "utf-8") as file:
			self.scene_file = json.load(file)
		self.eventqueue = iter(self.scene_file["main"]["events"])


	def update(self, scwidget): # ScWidget: DialogBox, ChoiceBox...
		try:
			self.current_event = next(self.eventqueue)
			self._event_type = self.current_event["event_type"]
			self.event_type = self.scene_file[self._event_type]
			self.current = self.event_type[self.current_event["item"]]
			self.error = False

		except StopIteration:
			self.error = True
		
		except:
			log_file = str(path.joinpath("Logs", "logs.txt"))
			with open(log_file, "r+", encoding="utf-8") as dosya:

				exc_type, exc_value, exc_traceback = sys.exc_info()
				traceback.print_tb(exc_traceback, limit=1, file=dosya)
				traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=dosya)

				dosya.write("\nTr: Böyle bir hata ile karşılaştığınız için özür dileriz. Sorununuzu çözmek ve başkalarının aynı hatayı yaşamasını önlemek için sizi discord sunucumuza davet ediyoruz.\nEn: We apologize for this error. We welcome you to our discord server to solve your problem and to prevent other people from experiencing the same error.\nhttps://discord.gg/BZ7zfKb")

			os.system(log_file)
			self.quit()
	
	def draw(self, screen_surface, image_dict):

		if self._event_type == "dialogEvents":
			char = f"{self.current['character']}_{self.current['pose']}_{self.current['emote']}"
			self.character_image = image_dict[char]
			self.character_image.set_alpha(125)
			self.character_image_resized = pg.transform.scale(self.character_image, (750,750))
			screen_surface.blit(self.character_image_resized, (350, 20))

		if self._event_type == "choiceEvents":
			print("choice eventi")





if __name__ == '__main__':
	path = pathlib.Path(__file__).resolve().parent
	json_path = str(path.joinpath("tests", "test.json"))
	Scene(json_path)
