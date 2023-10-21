from godot import exposed, export
from godot import *


@exposed
class Control(Control):
	def _ready(self):
		#Call godot command and change global value
		self.command = self.get_node("/root/Parallax_scene/my_godot")
		self.fighting_scene = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
	def _on_Again_pressed(self):
		self.command.set_hp("Player", 5)
		self.get_node("/root/Parallax_scene/Death_menu").visible = False
		self.fighting_scene.end_fight()
	def _on_Quit_pressed(self):
		self.get_tree().quit()
