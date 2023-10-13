from godot import exposed, export
from godot import *
import random

INPUT = ResourceLoader.load("res://TEXTURE/ENEMY_ENGER_CHIP.png")
OUTPUT = ResourceLoader.load("res://TEXTURE/BASE_ENERGY_CHIP.png")
STARTER = ResourceLoader.load("res://SLOTPREFAB/STARTER.tscn")

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
		for side in range(4):
			side += 1
			for _ in range(6):
				side_slots = self.get_child(side)
				centercontain = CenterContainer.new()
				centercontain.add_child(STARTER.instance())
				spi = Sprite.new()
				spi.set_offset(Vector2(32, 32))
				centercontain.add_child(spi)
				centercontain.set_pivot_offset(Vector2(32, 32))
				centercontain.set_rotation_degrees(180 if side == 2 else -90 if side == 3 else 90 if side == 4 else 0)
				print(centercontain.get_rotation())
				side_slots.add_child(centercontain)
		for side, slot in self.choosenslot:
			self._INPUT -= 1
			choosen = self.get_child(side).get_child(slot).get_child(1)
			choosen.set_texture(INPUT if self._INPUT >= 0 else OUTPUT)
			choosen.set_name("INPUT" if self._INPUT >= 0 else "OUTPUT")
		pass
