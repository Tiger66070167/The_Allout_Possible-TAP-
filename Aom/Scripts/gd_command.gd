extends Node2D


var is_fight_last = false
var last_shoot = false
onready var run_button = get_node("/root/Main/CanvasLayer/Node2D/CanvasLayer/run_button")
onready var node2d = get_node("/root/Main/CanvasLayer/Node2D")

func get_enemy_hp():
	return Globals.Enemy_Full_Health

func set_attack(entity, damage):
	pass

func is_fight_update():
	run_button.visible = not run_button.visible
	is_fight_last = Globals.is_fight

func shoot_update():
	Globals.shoot = false
	last_shoot = Globals.shoot
func _process(delta):
	if Globals.is_fight != is_fight_last:
		is_fight_update()
	if Globals.shoot != last_shoot:
		shoot_update()
