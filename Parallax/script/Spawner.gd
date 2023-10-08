extends Node2D

var Drone_path = preload("res://Parallax/Character_scene/Drone.tscn")
onready var Fighting_scene = get_node("/root/Parallax_scene/Upper_scene/Fighting_scene")
func _ready():
	pass
func spawn():
	"""this function will spawn enemy to Fighting scene"""
	var Drone = Drone_path.instance()
	Fighting_scene.add_child(Drone)
