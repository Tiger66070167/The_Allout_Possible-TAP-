from godot import exposed, export
from godot import *

@exposed
class ParallaxBackground(ParallaxBackground):
	"""Just controll parallax scrolling"""
	def _ready(self):
		pass
	def _process(self, delta):
		self.scroll_offset -= Vector2(self.moving_speed*delta, 0)
		
	def is_moving(self, moving, speed = 0):
		'''Start of Stop moving'''
		player_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
		if moving == False:
			player_anim.play("Idle")
			self.moving_speed = 0
		else:
			player_anim.play("Running")
			self.moving_speed = 50 + speed
