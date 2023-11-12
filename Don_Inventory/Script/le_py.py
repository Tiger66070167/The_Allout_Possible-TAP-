from godot import exposed, export
from godot import *
import random

@exposed
class le_py(Control):

	def _ready(self):
		self.inventory = self.get_node("/root/Main/CanvasLayer/Inventory_contianer")
		self.random_item()
	def random_item(self, amount=9):
		item_list = ["UPPER", "RIGHT", "LEFT", "DOWN"]
		random_item_list = random.choices(item_list, weights=[1, 1, 1, 1], k=amount)
		for i in range(len(random_item_list)):
			self.inventory.set_item_but_for_python(i, random_item_list[i])
