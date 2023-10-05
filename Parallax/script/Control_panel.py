from godot import exposed, export
from godot import *


@exposed
class Control_panel(Control):
	
	def _ready(self):
		#Prallax_path
		self.parallax = self.get_node("/root/Parallax_scene/Upper_scene/ParallaxBackground/")
		#Just_togglte_varl
		self.toggle = False
	def _on_Run_Button_pressed(self):
		self.toggle = not self.toggle
		self.parallax.is_moving(self.toggle)
