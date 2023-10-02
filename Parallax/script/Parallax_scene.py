from godot import exposed, export
from godot import *


@exposed
class Parallax_scene(Node2D):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')
	player_animate = get_node("Player_anim")
	
	def _ready(self):
		self.get_tree().paused = False
		player_animate.play("Running")


	def _process(self, delta):
		if Input.is_action_just_pressed("ESC"):
			self.get_tree().paused = not self.get_tree().paused
			self.get_node("Pause_menu").visible = not self.get_node("Pause_menu").visible
