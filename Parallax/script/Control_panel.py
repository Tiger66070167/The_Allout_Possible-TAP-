from godot import exposed, export
from godot import *


@exposed
class Control_panel(Control):
	
	def _ready(self):
		#Fight_scene_path
		self.Fighting_scene = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
		
		#Button node varieble
		self.start_fight = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/Fight_scene_Button")
		self.end_fight = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/End_fight")
		self.player_atk = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/P_Attack")
		self.enemy_atk = self.get_node("CenterContainer/VBoxContainer/HBoxContainer/E_Attack")
		self.spawn_enemy = self.get_node("CenterContainer/VBoxContainer/HBoxContainer2/Spawn_Enemy")
		
		self.command = self.get_node("/root/Parallax_scene/my_godot")
	def _process(self, delta):
		game_state = str(self.command.get_game_state())
		if game_state == "Running":
			self.button_visible(True, False, False, False, False)
		elif game_state == "Waiting":
			self.button_visible(False, True, False, False, True)
		elif game_state == "Fighting":
			self.button_visible(False, False, True, True, False)
	def _on_Fight_scene_Button_pressed(self):
		self.Fighting_scene.start_fight()
		
	def _on_P_Attack_pressed(self):
		self.Fighting_scene.player_attack()
		
	def _on_E_Attack_pressed(self):
		self.Fighting_scene.enemy_attack()
		
	def _on_Spawn_Enemy_pressed(self):
		self.Fighting_scene.spawn_enemy()
		
	def _on_End_fight_pressed(self):
		self.Fighting_scene.end_fight()
		
	def button_visible(self, st_f, en_f, p_atk, e_atk, spn_e):
		self.start_fight.visible = st_f
		self.end_fight.visible = en_f
		self.player_atk.visible = p_atk
		self.enemy_atk.visible = e_atk
		self.spawn_enemy.visible = spn_e
