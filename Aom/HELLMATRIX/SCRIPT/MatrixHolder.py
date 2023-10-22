from godot import exposed, export
from godot import *


@exposed
class MatrixHolder(Node2D):

	# member variables here, example:
	is_start = export(bool, default=False)

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
