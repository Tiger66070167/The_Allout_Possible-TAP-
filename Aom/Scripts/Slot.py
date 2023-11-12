from godot import exposed, export
from godot import *

WHITE = Color(255, 255, 255, 255)
CYAN = Color(0, 255, 255, 255)# up
BLACK = Color(0, 0, 0, 255)# down
PINK = Color(255, 0, 255, 255) # left
YELLOW = Color(255, 255, 0, 255) # right

NEW_BULLET = ResourceLoader.load("res://Scenes/Bullet.tscn")
@exposed
class Slot(Area2D):

	# member variables here, example:
	# a = export(int)
	# b = export(str, default='foo')
	can_set_tile = export(bool, default=False)
	mode = export(int, default=2)

	def _ready(self):
		self.add_to_group("slots") # set slot to slots group
	
	def _process(self, delta):
		self.texture_update()
	
	def tile_edit(self, status):
		self.can_set_tile = status
	
	def texture_update(self):
		"""update texture upon there mode"""
		texture_sprite = self.get_node("Sprite")
		if self.mode != 2:
			self.set_z_index(2)
		else:
			self.set_z_index(0)
		if self.mode == 2:
			texture_sprite.set_self_modulate(WHITE)
		elif self.mode == 3:
			texture_sprite.set_self_modulate(CYAN)
		elif self.mode == 4:
			texture_sprite.set_self_modulate(BLACK)
		elif self.mode == 5:
			texture_sprite.set_self_modulate(PINK)
		elif self.mode == 6:
			texture_sprite.set_self_modulate(YELLOW)
	
	def _on_slot_input(self, viewport, event, shapeidx):
		"""when mouse had event with slot"""
		if event.is_pressed() and event.get_button_index() == 1 and self.can_set_tile:
			if self.mode < 6:
				self.mode += 1
			else:
				self.mode = 2
