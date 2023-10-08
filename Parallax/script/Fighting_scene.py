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
		
		#Velocity for player pos
		self.velocity = Vector2()
		
		#Start with moving parallax
		self.parallax.is_moving(True)
	def _process(self, delta):
		#Player_pos it return Vector2 value
		self.player_pos = self.player.get_global_position()
		self.player.move_and_slide(self.velocity)
		
		#Condition for moving dron if in fight state
		if self.fight_state == True:
			self.Drone.move_and_slide(self.velocity)
			self.Drone_pos = self.Drone.get_global_position()
		
		#Check position for player
		self.position_check(self.player_pos, 500, 960, True)
		
	def start_fight(self):
		"""This function for toggle fighting_scene"""
		player_anim = self.player_anim
		if self.fight_state == True:
			self.fight_state = False
			self.Drone.queue_free()
			
			#let Player and parallax running again
			self.velocity.x = 200
			player_anim.play("Running")
		else:
			self.fight_state = True
			#Spawn Drone and setup all drone varlue
			self.spawner.spawn()
			self.Drone = self.get_child(1)
			self.Drone_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim")
			self.Drone_anim.flip_h = True
			
			#set parallax and player to move
			self.parallax.is_moving(True, 50)
			self.velocity.x = -200
			#stop player
			player_anim.play("Idle")
	def position_check(self, entity_position, l_border, r_border = 3000, is_player = False):
		"""This function is cheking for the position"""
		#this for stop player when out of scene
		if entity_position.x <= l_border and self.fight_state == True:
			self.velocity.x = 0
			if is_player == True:
				self.parallax.is_moving(False)
		elif entity_position.x >= r_border and self.fight_state == False:
			self.velocity.x = 0
			if is_player == True:
				self.parallax.is_moving(True)
