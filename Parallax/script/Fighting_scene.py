from godot import exposed, export
from godot import *


@exposed
class Fighting_scene(Node2D):

	def _ready(self):
		self.player = self.get_node("Upper_scene/Fighting_scene/Player")
	def _process(self, delta):
		pass
	def start_fight(self):
		"""This function for starting fight"""
