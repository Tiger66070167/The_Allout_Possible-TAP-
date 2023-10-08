from godot import exposed, export
from godot import *


@exposed
class Control_panel(Control):
	
	def _ready(self):
		#Fight_scene_path
		self.Fighting_scene = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
		
		#Button node varieble
		self.start_fight_button = self.get_node("CenterContainer/HBoxContainer/Fight_scene_Button")
		self.player_atk = self.get_node("CenterContainer/HBoxContainer/P_Attack")
		self.enemy_atk = self.get_node("CenterContainer/HBoxContainer/E_Attack")
		self.kill_enemy = self.get_node("CenterContainer/HBoxContainer/Kill_Enemy")
	def _on_Fight_scene_Button_pressed(self):
		self.Fighting_scene.start_fight()
		self.toggle_button_visible()
	def _on_P_Attack_pressed(self):
		pass
	def _on_E_Attack_pressed(self):
		pass
	def _on_Kill_Enemy_pressed(self):
		self.Fighting_scene.start_fight()
		self.toggle_button_visible()
	def toggle_button_visible(self):
		self.start_fight_button.visible = not self.start_fight_button.visible
		self.player_atk.visible = not self.player_atk.visible
		self.enemy_atk.visible = not self.enemy_atk.visible
		self.kill_enemy.visible = not self.kill_enemy.visible
