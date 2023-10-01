rom godot import exposed, export
from godot import *

@exposed
class Parallax_scene(Node2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		self.Pause_menu = self.get_node("Pause_menu")
	def _process(self, delta):
		if Input.is_action_pressed("ESC") == True:
			@Pause_menu.visible = not Pause_menu.visible
