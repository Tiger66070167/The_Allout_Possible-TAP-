from godot import exposed, export
from godot import *


@exposed
class Globals(Node):
	item_list = {"Screen_moving_x" : 40}
	def _ready(self):
		pass
		
	def call_value_item(self, item):
		return self.item_list[item]
