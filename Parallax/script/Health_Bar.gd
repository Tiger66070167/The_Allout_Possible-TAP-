extends Node2D

onready var player_hb = get_node("Player_Health_Bar")
onready var enemy_hb = get_node("Enemy_Health_Bar")
var full_heart = preload("res://Parallax/Asset/UI/Full_health.png")
var empty_heart = preload("res://Parallax/Asset/UI/Empty_health.png")
func _ready():
	pass
func _process(_delta):
	player_health_update()
	if get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").get_child_count() == 2:
		$Enemy_Health_Bar.visible = true
	else:
		$Enemy_Health_Bar.visible = false
	enemy_health_update()
func player_health_update():
	for i in player_hb.get_child_count():
		if i < Globals.Player_Health:
			player_hb.get_child(i).set_texture(full_heart)
		else:
			player_hb.get_child(i).set_texture(empty_heart)
func enemy_health_update():
	for i in enemy_hb.get_child_count():
		enemy_hb.get_child(i).visible = i<Globals.Enemy_Full_Health
		if i < Globals.Enemy_Health:
			enemy_hb.get_child(i).set_texture(full_heart)
		else:
			enemy_hb.get_child(i).set_texture(empty_heart)
