from godot import exposed, export
from godot import *
@exposed
class Parallax_scene(Node2D):

	def _ready(self):
		#Player_animate
		player_anim = self.get_node("Upper_scene/Fighting_scene/Player/Player_anim")
		#Drone_animate
		Drone_anim = self.get_node("Upper_scene/Fighting_scene/Drone/Drone_anim")
	
		
		#Heart_for_display
		self.Heart = 3
		
		
		
		
		#Setup_animate_for_start_up_game
		self.get_tree().paused = False
		player_anim.play("Idle")
		Drone_anim.set_flip_h(True)
		
	def _process(self, delta):
		#Pause_binding
		if Input.is_action_just_pressed("ESC"):
			self.get_tree().paused = not self.get_tree().paused
			self.get_node("Pause_menu").visible = not self.get_node("Pause_menu").visible
