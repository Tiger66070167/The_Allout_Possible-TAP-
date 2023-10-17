extends Node2D

var Drone_path = preload("res://Parallax/Character_scene/Drone.tscn")
onready var Fighting_scene = get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
func _ready():
	pass
func spawn():
	"""this function will spawn enemy to Fighting scene"""
	Fighting_scene.add_child(Drone_path.instance())
	Globals.Enemy_Health = 5
func get_player_hp():
	return Globals.Player_Health
func get_enemy_hp():
	return Globals.Enemy_Health
func get_game_state():
	return Globals.game_state
func set_game_state(state):
	Globals.game_state = state
