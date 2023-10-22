from godot import exposed, export
from godot import *


@exposed
class Button(Button):
	def _pressed(self):
		self.get_parent().is_start = True

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
