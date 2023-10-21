extends Node2D

onready var player_hb = get_node("Player_Health_Bar")
onready var enemy_hb = get_node("Enemy_Health_Bar")
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
		player_hb.get_child(i).visible = Globals.Player_Health > i
func enemy_health_update():
	for i in enemy_hb.get_child_count():
		enemy_hb.get_child(i).visible = Globals.Enemy_Health > i
