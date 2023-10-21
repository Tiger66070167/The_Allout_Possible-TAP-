extends Node2D


var enemy_path = {"Drone":preload("res://Parallax/Character_scene/Drone.tscn"), \
				"Ball_guy":preload("res://Parallax/Character_scene/Ball_guy.tscn"), \
				"Hammer_dude":preload("res://Parallax/Character_scene/Hammer_dude.tscn")}
onready var Fighting_scene = get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
func _ready():
	pass
func spawn(enemy=Globals.enemy_wave[0]):
	"""this function will spawn enemy to Fighting scene"""
	if str(enemy) == "null":
		pass
	else:
		Fighting_scene.add_child(enemy_path[enemy].instance())
		Globals.Enemy_Health = 5
func get_player_hp():
	return Globals.Player_Health
	
func get_enemy_hp():
	return Globals.Enemy_Health
	
func get_game_state():
	return Globals.game_state
	
func set_game_state(state):
	Globals.game_state = state
	
func get_hp(entity):
	if entity == "Player":
		return Globals.Player_Health
	elif entity == "Enemy":
		return Globals.Enemy_Health
		
func set_hp(entity, value):
	if entity == "Player":
		Globals.Player_Health = value
	elif entity == "Enemy":
		Globals.Enemy_Health = value
	else:
		print("Error")
		
func get_enemy_wave():
	return Globals.enemy_wave
	
func set_enemy_wave(enemy, remove = false):
	if remove == true:
		Globals.enemy_wave.remove(0)
	else:
		Globals.enemy_wave.append(enemy)

func new_wave():
	Globals.new_wave()
