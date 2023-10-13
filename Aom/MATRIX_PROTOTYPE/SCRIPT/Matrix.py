from godot import exposed, export
from godot import *
import random

INPUT = ResourceLoader.load("res://TEXTURE/ENEMY_ENGER_CHIP.png")
OUTPUT = ResourceLoader.load("res://TEXTURE/BASE_ENERGY_CHIP.png")

@exposed
class Matrix(Control):
	_INPUT = 3
	_OUTPUT = 2
	choosenslot = [(side+1, slot) for side in range(4) for slot in range(6)]
	choosenslot = random.sample(choosenslot, k=_INPUT+_OUTPUT)

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		for side, slot in self.choosenslot:
			self._INPUT -= 1
			slot = self.get_child(side).get_child(slot).get_node("SLOT")
			slot.set_texture(INPUT if self._INPUT >= 0 else OUTPUT)
			slot.set_name("INPUT" if self._INPUT >= 0 else "OUTPUT")
		pass
