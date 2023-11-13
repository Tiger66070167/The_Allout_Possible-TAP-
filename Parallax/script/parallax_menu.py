from godot import exposed, export
from godot import *

@exposed
class ParallaxBackground(ParallaxBackground):
	"""Just controll parallax scrolling"""
	def _ready(self):
		self.moving_speed = 140
		
	def _process(self, delta):
		self.scroll_offset -= Vector2(self.moving_speed*delta, 0)
