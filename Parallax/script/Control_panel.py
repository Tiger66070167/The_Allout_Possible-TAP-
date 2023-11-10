from godot import exposed, export
from godot import *


@exposed
class Control_panel(Control):
	
	def _ready(self):
		#Fight_scene_path
		self.Fighting_scene = self.get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene")
		
		#Button node varieble
		self.start_fight = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/Fight_scene_Button")
		self.player_atk = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/P_Attack")
		self.enemy_atk = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/E_Attack")
		
		self.command = self.get_node("/root/Main/Parallax_scene/my_godot")
	def _process(self, delta):
		game_state = str(self.command.get_game_state())
		if game_state == "Running":
			self.button_visible(True, False, False)
		elif game_state == "Waiting":
			self.button_visible(False, False, False)
		elif game_state == "Fighting":
			self.button_visible(False, True, True)
	def _on_Fight_scene_Button_pressed(self):
		self.Fighting_scene.start_fight()
		self.Fighting_scene.is_done_toggle()
		self.command.new_wave()
		
	def _on_P_Attack_pressed(self):
		self.Fighting_scene.player_attack()
		
	def _on_E_Attack_pressed(self):
		self.Fighting_scene.enemy_attack() 
		
	def button_visible(self, st_f, p_atk, e_atk):
		self.start_fight.visible = st_f
		self.player_atk.visible = p_atk
		self.enemy_atk.visible = e_atk
