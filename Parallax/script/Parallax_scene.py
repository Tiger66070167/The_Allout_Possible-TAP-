from godot import exposed, export
from godot import *


@exposed
class Parallax_scene(Node2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		self.get_tree().paused = False
		
	def _process(self, delta):
		if Input.is_action_just_pressed("ESC"):
			self.get_tree().paused = not self.get_tree().paused
			self.get_node("Pause_menu").visible = not self.get_node("Pause_menu").visible
