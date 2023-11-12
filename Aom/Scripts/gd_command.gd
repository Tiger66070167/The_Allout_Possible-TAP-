extends Node2D


var is_fight_last = false
var last_shoot = false

var shooted_bullet = 0

onready var locker = get_node("/root/Main/CanvasLayer/Node2D/CanvasLayer/Locker")
onready var run_button = get_node("/root/Main/CanvasLayer/Node2D/CanvasLayer/run_button")
onready var node2d = get_node("/root/Main/CanvasLayer/Node2D")

func bullet_update():
	shooted_bullet += 1
	
func get_enemy_hp():
	return Globals.Enemy_Full_Health

func get_just_set():
	return Globals.just_set

func toggle_just_set():
	Globals.just_set = false

func is_fight_update():
	run_button.visible = not run_button.visible
	is_fight_last = Globals.is_fight

func shoot_update():
	Globals.shoot = false
	last_shoot = Globals.shoot

func _process(_delta):
	if Globals.is_fight != is_fight_last:
		is_fight_update()
	if Globals.shoot != last_shoot:
		shoot_update()
	if shooted_bullet >= 3:
		locker.visible = false
		Globals.is_shoot = not Globals.is_shoot
		shooted_bullet = 0
