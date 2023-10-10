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
		if moving == False:
			self.moving_speed = 0
		else:
			self.moving_speed = 50 + speed
