from godot import exposed, export
from godot import *


@exposed
class Control_panel(Control):
	
	def _ready(self):
		#Fight_scene_path
		self.Fighting_scene = self.get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene")
		
		#Button node varieble
		self.start_fight = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/CanvasLayer/Start_fight")
		
		self.command = self.get_node("/root/Main/Parallax_scene/my_godot")

	def _on_Start_fight_button_down(self):
		self.Fighting_scene.start_fight()
		self.Fighting_scene.is_done_toggle()
		self.command.new_wave()
		self.start_fight.visible = False
