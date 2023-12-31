from godot import exposed, export
from godot import *

SPEED = 50
EMPTY = ResourceLoader.load("res://Texture/Empty.png")

@exposed
class Projectile(Area2D):

	isit_start = False
	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		pass
	def _process(self, delta):
		self.isit_start = self.get_parent().get_parent().get_parent().get_parent().is_start
		side = str(self.get_parent().get_parent().get_name())
		if self.isit_start:
			if side == "Upper":
				self.move_local_y(delta*SPEED)
			elif side == "Lower":
				self.move_local_y(delta*-SPEED)
			elif side == "Left":
				self.move_local_x(delta*SPEED)
			elif side == "Right":
				self.move_local_x(delta*-SPEED)

	def _on_Projectile_area_entered(self, area):
		areaname = str(area.status)
		if self.isit_start:
			if areaname in ("Empty_Slot", "Shooter") and self.isit_start:
				self.queue_free()
			elif areaname == "Target":
				print(area.get_name())
				area.texture_change(EMPTY, "Empty_Slot")
				self.queue_free()
			elif areaname == "Turn":
				self.set_rotation_degrees(-area.get_rotation_degrees())
				
