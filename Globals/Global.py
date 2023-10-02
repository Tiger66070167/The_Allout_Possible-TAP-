from godot import exposed, export
from godot import *


@exposed
class Global(Node):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	
	#It for how fast parallax would move
	Screen_moving_x = 40
	
	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
