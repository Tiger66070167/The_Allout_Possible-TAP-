from godot import exposed, export
from godot import *

BULLET_SPEED = 150

@exposed
class Bullet(Area2D):

	# member variables here, example:
	#a = export(int)
	#b = export(str, default='foo')
	bullet_hp = export(int, default=4)
	mode = export(int, default=-2)
	found_tile = False
	
	movement = export(Vector2, default=Vector2())

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.add_to_group("bullets")
		self.command = self.get_node("/root/Main/CanvasLayer/Node2D/gd_command")

	def _process(self, delta):
		delta_speed = delta*BULLET_SPEED # bullet_delta_speed
		if self.found_tile:
			self.set_position(self.get_position().move_toward(Vector2.ZERO, delta_speed))
			if self.get_position() == Vector2.ZERO:
				self.found_tile = False
		else:
			self.translate(self.movement*delta_speed)
	
	def _on_bullet_entered(self, target):
		"""when bullet collide with other area"""
		if self not in target.get_children():# collide with other
			if target.mode in (0, 1): # collid with starter or empty starter
				self.command.bullet_update()
				self.queue_free()
			elif target.mode == -1: # collide with negative 
				target.mode = 0 # set negative to empty
				#self.get_node("/root/").get_child(0).check_enemy() # call check enemy
				self.command.bullet_update()
				self.queue_free()
			elif target.mode > 2: # collide with special tile
				if self.bullet_hp == 0:
					self.command.bullet_update()
					self.queue_free()
				self.bullet_hp -= 1
				global_now = self.get_global_position() # collect global pos
				
				self.get_parent().call_deferred("remove_child", self)#remove_child(self)# remove yourself from parent
				target.call_deferred("add_child", self)#add_child(self)# be child of new parent
				
				self.set_position(target.to_local(global_now))# set position to reletive with old
				self.found_tile = True
				self.movement = self.tile_function(target.mode)
				
	def tile_function(self, modeid):
		"""tile function"""
		if modeid == 3:
			return Vector2.UP
		elif modeid == 4:
			return Vector2.DOWN
		elif modeid == 5:
			return Vector2.LEFT
		elif modeid == 6:
			return Vector2.RIGHT

