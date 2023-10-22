from godot import exposed, export
from godot import *
import random

SHOOTER = ResourceLoader.load("res://Texture/Shooter.png")
TARGET = ResourceLoader.load("res://Texture/Target.png")
PROJECTILE = ResourceLoader.load("res://NODE/Projectile.tscn")

all_slot = [(side, i) for i in range(6) for side in ("Upper", "Lower", "Left", "Right")]

@exposed
class SideBar(Node2D):
	
	def generate_slot(self, Shooter=2, Target=1):
		all_target = Shooter+Target
		selected_slot = random.sample(all_slot, k=all_target)
		for i in range(all_target):
			side, slot = selected_slot[i]
			if Shooter > 0:
				ShooterSlot = self.get_node(side).get_child(slot)
				Projectile = PROJECTILE.instance()
				ShooterSlot.add_child(Projectile)
				ShooterSlot.texture_change(SHOOTER, "Shooter")
			else:
				self.get_node(side).get_child(slot).texture_change(TARGET, "Target")
			Shooter -= 1

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.generate_slot(2, 2)
		pass
			
