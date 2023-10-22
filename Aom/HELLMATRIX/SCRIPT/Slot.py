from godot import exposed, export
from godot import *

EMPTY_SLOT = ResourceLoader.load("res://Texture/Empty.png")
ARROW = ResourceLoader.load("res://Texture/Arrow.png")

@exposed
class Slot(Area2D):

	# member variables here, example:
	status = export(str, default="Empty")
	
	def texture_change(self, _texture=EMPTY_SLOT, value="Empty"):
		self.status = value
		self.get_node("TextureButton").set_normal_texture(_texture)
		
	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		name = str(self.get_parent().get_name())
		if name == "Grid":
			self.texture_change()
		else:
			self.texture_change(value="Empty_Slot")
		pass
	row = 90
	def _on_button_pressed(self):
		sta = str(self.status)
		if self.row == 360:
			self.texture_change(EMPTY_SLOT, "Empty")
			self.set_rotation_degrees(0)
			self.row = 90
		elif sta == "Empty":
			self.texture_change(ARROW, "Turn")
		elif sta == "Turn":
			self.set_rotation_degrees(self.row)
			self.row += 90
