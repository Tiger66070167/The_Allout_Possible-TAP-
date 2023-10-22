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
		#Call godot command and change global value
		self.command = self.get_node("/root/Parallax_scene/my_godot")
		#Velocity for player pos
		self.enemy_target_pos = {"Fighting":Vector2(1300, 450), "Attack":Vector2(830, 450)}
		self.player_target_pos = {"Running":Vector2(960, 450), "Fighting":Vector2(650, 450), "Attack":Vector2(1200, 450)}

		#Setup start
		self.parallax.is_moving(False)
		self.player.move_to_position(self.player_target_pos.get("Running"), 600)
		self.player_anim.play("Running")
		
		#Setup Fighting state
		self.fighting_state = False
		
		#Setup player and enemy state
		self.player_state = "Running"
		self.enemy_state = "Null"
		
		#this value if for checking the animation if is done
		self.is_done = False
		self.clock = 0
		self.another_clock = 0
		
	def _process(self, delta):
		player_pos = self.player.get_position()
		enemy_health = self.command.get_hp("Enemy")
		#Enemy contition
		if self.get_child_count() == 2:
			self.command.set_game_state("Fighting")
			enemy_pos = self.enemy.get_position()
			if enemy_health <= 0:
				self.kill_enemy()
			if enemy_pos == self.enemy_target_pos.get("Fighting") and self.enemy_state == "Fighting" and self.another_clock == 0:
				self.enemy_anim.flip_h = True
				self.enemy_anim.play("Idle")
				self.another_clock = 1
			elif enemy_pos == self.enemy_target_pos.get("Attack") and self.enemy_state == "Attacking" and self.another_clock == 0:
				if not self.is_done:
					self.enemy_anim.play("Attack")
				if self.is_done:
					self.enemy.move_to_position(self.enemy_target_pos.get("Fighting"), 500)
					self.enemy_anim.flip_h = False
					self.is_done = False
					self.enemy_state = "Fighting"
					self.another_clock = 0
		elif player_pos == self.player_target_pos.get("Fighting") and self.get_child_count() != 2:
			self.command.set_game_state("Waiting")
		elif player_pos == self.player_target_pos.get("Running"):
			self.command.set_game_state("Running")
		#Player Condition
		if player_pos == self.player_target_pos.get("Fighting") and self.player_state == "Fighting" and self.clock == 0:
			self.player_anim.flip_h = False
			self.player_anim.play("Idle")
			self.clock = 1
			if self.enemy_state == "Death":
				self.command.set_enemy_wave("-", True)
				self.is_done_toggle()
		elif player_pos == self.player_target_pos.get("Attack") and self.player_state == "Attacking" and self.clock == 0:
			if not self.is_done:
				self.player_anim.play("Attack")
			if self.is_done:
				self.player_anim.flip_h = True
				self.player.move_to_position(self.player_target_pos.get("Fighting"), 400)
				self.player_state = "Fighting"
				self.is_done = False
				self.clock = 0
		elif player_pos == self.player_target_pos.get("Running") and self.player_state == "Running":
			self.parallax.is_moving(True)
		if len(self.command.get_enemy_wave()) == 1:
			self.end_fight()
		elif self.get_child_count() != 2 and self.is_done:
				self.spawn_enemy()
				self.is_done = False
	def start_fight(self):
		"""This function for toggle fighting_scene"""
		if self.fighting_state == False:
			self.fighting_state = True
			
			self.clock = 0
			
			self.player_anim.flip_h = True
			
			#Move everyone to fighting positon
			self.player.move_to_position(self.player_target_pos.get("Fighting"), 400)
			
			#Set running to all
			self.player_anim.play("Running")
			
			#Set state to all
			self.player_state = "Fighting"
			self.parallax.is_moving(False)
	def spawn_enemy(self):
		"""create enemy"""
		enemy_anim_path = {"Drone":"/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim/", \
		"Ball_guy":"/root/Parallax_scene/Upper_scene/Fighting_scene/Ball_guy/Ball_anim/", \
		"Hammer_dude":"/root/Parallax_scene/Upper_scene/Fighting_scene/Hammer_dude/Hammer_anim/"}
		enemy_path = {"Drone":"/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/", \
		"Ball_guy":"/root/Parallax_scene/Upper_scene/Fighting_scene/Ball_guy/", \
		"Hammer_dude":"/root/Parallax_scene/Upper_scene/Fighting_scene/Hammer_dude/"}
		
		enemy = str(list(self.command.get_enemy_wave())[0])
		spawner = self.get_node("/root/Parallax_scene/my_godot")
		spawner.spawn()
		
		self.another_clock = 0
		self.enemy = self.get_node(enemy_path[enemy])
		self.enemy_anim = self.get_node(enemy_anim_path[enemy])
		self.enemy_anim.flip_h = True
		self.enemy_anim.play("Running")
		self.enemy_state = "Fighting"
		
		self.enemy.move_to_position(self.enemy_target_pos.get("Fighting"), 500)
		
	def end_fight(self):
		if self.get_child_count() == 2:
				self.kill_enemy()
		if self.fighting_state == True:
			self.fighting_state = False
			
			self.clock = 0
			self.another_clock = 0
			self.player_state = "Running"
			self.player_anim.play("Running")
			self.player.move_to_position(self.player_target_pos.get("Running"), 400)
	def player_attack(self):
		self.move_child(self.enemy, 1)
		self.move_child(self.player, 2)
		self.player.move_to_position(self.player_target_pos.get("Attack"), 400)
		self.player_anim.play("Running")
		self.player_state = "Attacking"
		self.clock = 0
		self.another_clock = 0
		
	def enemy_attack(self):
		self.move_child(self.player, 1)
		self.move_child(self.enemy, 2)
		self.enemy.move_to_position(self.enemy_target_pos.get("Attack"), 500)
		self.enemy_anim.play("Running")
		self.enemy_state = "Attacking"
		self.clock = 0
		self.another_clock = 0
	def kill_enemy(self):
		self.enemy_state = "Death"
		self.enemy_anim.play("Death")
	def is_done_toggle(self):
		self.is_done = True
