from godot import exposed, export
from godot import *

WHITE = Color(255, 255, 255, 255)
GREEN = Color(0, 255, 0, 255)
RED = Color(255, 0, 0, 255)

BULLET = ResourceLoader.load("res://Scenes/Bullet.tscn")

@exposed
class Starter(Area2D):

	# member variables here, example:
	# a = export(int)
	# b = export(str, default='foo')
	mode = export(int, default=0)

	def _ready(self):
		self.add_to_group("starters")
	
	def _process(self, delta):
		self.texture_update()
	
	def run_bullets(self):
		"""make bullet running"""
		if self.mode == 1:# positive mode
			bullet = BULLET.instance()
			if str(self.get_parent().get_name()) == "upper":
				bullet.movement = Vector2.DOWN
			elif str(self.get_parent().get_name()) == "lower":
				bullet.movement = Vector2.UP
			elif str(self.get_parent().get_name()) == "right":
				bullet.movement = Vector2.LEFT
			elif str(self.get_parent().get_name()) == "left":
				bullet.movement = Vector2.RIGHT
			self.add_child(bullet)
	
	def texture_update(self):
		"""update texture"""
		if self.mode == 0:
			self.set_modulate(WHITE)
		elif self.mode == 1:
			self.set_modulate(GREEN)
		elif self.mode == -1:
			self.set_modulate(RED)
	
