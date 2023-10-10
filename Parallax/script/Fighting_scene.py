from godot import exposed, export
from godot import *


@exposed
class Fighting_scene(Node2D):
	"""This Function is for controling Fighting scene"""
	def _ready(self):
		"""Define all value and Path for every here **Discripe on top of the value**"""
		#Player_path **Not animate sprite**
		self.player = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Player")
		#Player_ainmate_path
		self.player_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
		#Prallax_path
		self.parallax = self.get_node("/root/Parallax_scene/Upper_scene/ParallaxBackground/")
		#spawner_path
		self.spawner = self.get_node("/root/Parallax_scene/Spawner")
		
		#set fight_state
		self.fight_state = False
		self.is_done = False
		self.counter = 0
		
		#Velocity for player pos
		self.enemy_target_pos = {"Fighting":Vector2(1300, 450)}
		self.player_target_pos = {"Main":Vector2(960, 450), "Fighting":Vector2(650, 450), "Attack":Vector2(1180, 450)}
		
		#Setup start
		self.parallax.is_moving(True)
		self.player_anim.play("Running")
	def _process(self, delta):
		player_pos = self.player.get_position()
		if player_pos == self.player_target_pos.get("Fighting"):
			self.player_anim.play("Idle")
			self.parallax.is_moving(False)
			self.player_anim.flip_h = False
		elif player_pos == self.player_target_pos.get("Attack"):
			self.player_anim.flip_h = False
			if str(self.player_anim.get_animation()) != "Shoot" and self.counter == 0:
				self.counter += 1
				self.player_anim.play("Shoot")
			if self.is_done == True:
				self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Effect").play("Gun_Hit")
				self.counter = 0
				self.is_done = False
				self.player_anim.flip_h = True
				self.player_fighting()
		elif player_pos == self.player_target_pos.get("Main") and self.fight_state == False:
			self.parallax.is_moving(True)
			self.player_anim.play("Running")
			self.player_anim.flip_h = False
		else:
			self.player_anim.play("Running")
			
		if self.fight_state == True:
			enemy_pos = self.Drone.get_position()
			if enemy_pos == self.enemy_target_pos.get("Fighting"):
				self.Drone_anim.play("Idle")
			else:
				self.Drone_anim.play("Running")
	def start_fight(self):
		"""This function for toggle fighting_scene"""
		player_anim = self.player_anim
		if self.fight_state == True:
			self.fight_state = False
			
			#let Player and parallax running again
			player_anim.play("Running")
			self.player_main()
		else:
			self.fight_state = True
			#Spawn Drone and setup all drone varlue
			self.spawner.spawn()
			self.Drone = self.get_child(1)
			self.Drone_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim")
			self.Drone_anim.flip_h = True
			self.player_anim.flip_h = True
			
			self.player_fighting()
			self.Drone.move_to_position(self.enemy_target_pos.get("Fighting"), 300)
			#set parallax and player to move
			self.parallax.is_moving(False)
	def player_attack(self):
		self.player.move_to_position(self.player_target_pos.get("Attack"), 240)
	def player_fighting(self):
		self.player.move_to_position(self.player_target_pos.get("Fighting"), 240)
	def player_main(self):
		self.player.move_to_position(self.player_target_pos.get("Main"), 200)
	def is_done_toggle(self):
		self.is_done = not self.is_done
