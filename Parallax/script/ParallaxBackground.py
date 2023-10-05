from godot import exposed, export
from godot import *

@exposed
class ParallaxBackground(ParallaxBackground):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		#player_animate
		self.parallax_anim = self.get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
		
		#Moving_speed
		self.moving_speed = 0
	
	def _process(self, delta):
		self.scroll_offset -= Vector2(self.moving_speed*delta, 0)
	
	def is_moving(self, moving):
		'''Start of Stop moving'''
		if moving == False:
			self.parallax_anim.play("Idle")
			self.moving_speed = 0
		else:
			self.parallax_anim.play("Running")
			self.moving_speed = 50
