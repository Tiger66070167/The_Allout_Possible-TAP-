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
		
		#Velocity for player pos
		self.enemy_target_pos = {"Fighting":Vector2(1300, 450), "Attack":Vector2(730, 450)}
		self.player_target_pos = {"Main":Vector2(960, 450), "Fighting":Vector2(650, 450), "Attack":Vector2(1250, 450)}

		#Setup start
		self.parallax.is_moving(True)
		self.player_anim.play("Running")
		
		#Setup Fighting state
		self.fighting_state = False
		
		#Setup player and enemy state
		self.player_state = "Running"
		self.enemy_state = "Null"
		
		#this value if for checking the animation if is done
		self.is_done = False
		
	def _process(self, delta):
		player_pos = self.player.get_position()
		
		#Enemy contition
		if self.get_child_count() == 2:
			enemy_pos = self.enemy.get_position()
			if enemy_pos == self.enemy_target_pos.get("Fighting") and self.enemy_state == "Fighting":
				self.enemy_anim.flip_h = True
				self.enemy_anim.play("Idle")
			elif enemy_pos == self.enemy_target_pos.get("Attack") and self.enemy_state == "Attacking":
				self.enemy_anim.play("Attack")
				if self.is_done:
					self.enemy.move_to_position(self.enemy_target_pos.get("Fighting"), 300)
					self.enemy_anim.flip_h = False
					self.is_done = False
					self.enemy_state = "Fighting"
			elif self.enemy_state == "Death":
				self.enemy_anim.play("Death")
				if self.is_done:
					self.player.move_to_position(self.player_target_pos.get("Main"), 400)
					self.player_anim.play("Running")
					self.player_state = "Running"
					self.is_done = False
			else:
				self.enemy_anim.play("Running")
		#Player Condition
		if player_pos == self.player_target_pos.get("Fighting") and self.player_state == "Fighting":
			self.player_anim.flip_h = False
			self.player_anim.play("Idle")
		elif player_pos == self.player_target_pos.get("Attack") and self.player_state == "Attacking":
			self.player_anim.play("Attack")
			if self.is_done:
				self.player_anim.flip_h = True
				self.player.move_to_position(self.player_target_pos.get("Fighting"), 400)
				self.player_state = "Fighting"
				self.is_done = False
		elif player_pos == self.player_target_pos.get("Main") and self.player_state == "Running":
			self.parallax.is_moving(True)
		else:
			self.player_anim.play("Running")
	def start_fight(self):
		"""This function for toggle fighting_scene"""
		spawner = self.get_node("/root/Parallax_scene/Spawner")
		if self.fighting_state == False:
			self.fighting_state = True
			
			#spawn enemy
			spawner.spawn()
			
			#creat enemy
			self.enemy = self.get_child(1)
			self.enemy_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim/")
			self.enemy_anim.flip_h = True
			self.player_anim.flip_h = True
			
			#Move everyone to fighting positon
			self.enemy.move_to_position(self.enemy_target_pos.get("Fighting"), 300)
			self.player.move_to_position(self.player_target_pos.get("Fighting"), 400)
			
			#Set running to all
			self.enemy_anim.play("Running")
			self.player_anim.play("Running")
			
			#Set state to all
			self.player_state = "Fighting"
			self.enemy_state = "Fighting"
			self.parallax.is_moving(False)
	def end_fight(self):
		if self.fighting_state == True:
			self.fighting_state = False
			
			self.enemy_anim.play("Death")
			
			self.enemy_state = "Death"
	
	def player_attack(self):
		self.player.move_to_position(self.player_target_pos.get("Attack"), 400)
		self.player_anim.play("Running")
		self.player_state = "Attacking"

	def enemy_attack(self):
		self.enemy.move_to_position(self.enemy_target_pos.get("Attack"), 300)
		self.enemy_anim.play("Running")
		self.enemy_state = "Attacking"
		
	def is_done_toggle(self):
		self.is_done = True
