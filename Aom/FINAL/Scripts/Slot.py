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
		self.add_to_group("slots")
		pass
	
	def _process(self, delta):
		self.texture_update()
	
	def tile_edit(self, status):
		self.can_set_tile = status
	
	def texture_update(self):
		"""update texture upon there mode"""
		if self.mode != 2:
			self.set_z_index(2)
		else:
			self.set_z_index(0)
		if self.mode == 2:
			self.set_modulate(WHITE)
		elif self.mode == 3:
			self.set_modulate(CYAN)
		elif self.mode == 4:
			self.set_modulate(BLACK)
		elif self.mode == 5:
			self.set_modulate(PINK)
		elif self.mode == 6:
			self.set_modulate(YELLOW)
	
	def _on_slot_input(self, viewport, event, shapeidx):
		"""when mouse had event with slot"""
		if event.is_pressed() and event.get_button_index() == 1 and self.can_set_tile:
			if self.mode < 6:
				self.mode += 1
			else:
				self.mode = 2
	'''
	def _on_bullet_entered(self, bullet):
		"""when bullet collide"""
		if self.mode == 2 or bullet in self.get_children():
			return
		new_bullet = NEW_BULLET.instance()
		if self.mode == 4: # move down
			new_bullet.movement_y = 1
		elif self.mode == 3: # move up
			new_bullet.movement_y = -1
		elif self.mode == 5: # move left
			new_bullet.movement_x = -1
		elif self.mode == 6: # move right
			new_bullet.movement_x = 1
		#self.add_child(new_bullet)
	'''
