from godot import exposed, export
from godot import *
import random

inventory = ResourceLoader.load("res://Don_Inventory/Resource/Inventory.tres")
high_way = ResourceLoader.load("res://Main Scene/resource/new_resource.tres")
@exposed
class Node2D(Node2D):

	positive_num = export(int, default=3)
	negative_num = export(int, default=3)
	def _ready(self):
		high_way.connect("set", self, "_on_set")
		high_way.connect("set", self, "_on_set")
		self.gd_command = self.get_node("gd_command")
		self.locker = self.get_node("CanvasLayer/Locker")
		
	def _on_reset(self):
		"""when click reset"""
		self.reset_all() # reset all starters slots and bullets
		
	def _on_set(self):
		"""when click set"""
		self.reset_all() # reset all starters slots and bullets
		self.get_tree().call_group("slots", "tile_edit", True) # activate slots modifine
		self.random_starter(self.positive_num, self.negative_num) # create starter
	
	def _on_run(self):
		"""when click run"""
		self.gd_command.shoot_toggle()
		self.item_update()
		self.get_tree().call_group("starters", "run_bullets") # make bullet run
		self.get_tree().call_group("slots", "tile_edit", False) # disable slots midifine
	
	def random_starter(self, positive, negative):
		"""genrate random starters"""
		positive = high_way.get_enemy_hp()
		negative = high_way.get_enemy_hp()
		positive = 12 if positive > 12 else positive# limit
		negative = 12 if negative > 12 else negative
		
		all_slot = [(side, slot) for slot in range(6) for side in range(4)]# (0-3, 0-5)
		selected = random.sample(all_slot, positive+negative)
		for side, slot in selected:
			if positive > 0:
				positive -= 1
				self.get_child(side).get_child(slot).mode = 1
			else:
				self.get_child(side).get_child(slot).mode = -1
	
	def reset_all(self):
		"""reset everthing"""
		self.get_tree().call_group("bullets", "queue_free")
		for side in range(4):
			for slot in range(6):
				self.get_child(side).get_child(slot).mode = 0
		for slot in self.get_child(4).get_children():
			slot.mode = 2
		self.get_tree().call_group("slots", "tile_edit", False)

	def check_enemy(self):
		"""check enemy"""
		enemy_left = 0
		for side in range(4):
			for slot in range(6):
				if self.get_child(side).get_child(slot).mode == -1:
					enemy_left += 1
		return enemy_left

	def item_update(self):
		for item_index in range(36):
			if inventory.items[item_index+9]:
				item = str(inventory.items[item_index+9].name)
				if item == "UPPER":
					self.get_node("Grid").get_child(item_index).mode = 3
				elif item == "DOWN":
					self.get_node("Grid").get_child(item_index).mode = 4
				elif item == "LEFT":
					self.get_node("Grid").get_child(item_index).mode = 5
				elif item == "RIGHT":
					self.get_node("Grid").get_child(item_index).mode = 6
			else:
				self.get_node("Grid").get_child(item_index).mode = 2
