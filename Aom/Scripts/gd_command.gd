extends Node2D


var is_fight_last = false
var last_shoot = false
var shooted_bullet = 0

var high_way = preload("res://Main Scene/resource/new_resource.tres")
var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")

onready var locker = get_node("/root/Main/CanvasLayer/Node2D/CanvasLayer/Locker")
onready var run_button = get_node("/root/Main/CanvasLayer/Node2D/CanvasLayer/run_button")
onready var node2d = get_node("/root/Main/CanvasLayer/Node2D")

func _ready():
	high_way.connect("player_atked", self, "e_atk")
	high_way.connect("enemy_atked", self, "e_atked")
func shoot_toggle():
	run_button.visible = not run_button.visible
	locker.visible = not locker.visible

func bullet_update():
	shooted_bullet += 1

func get_damage():
	var tile_left = node2d.check_enemy()
	var enemy_health = Globals.Enemy_Health
	return abs(tile_left-enemy_health)

func _process(_delta):
	if Globals.is_fight != is_fight_last:
		shoot_toggle()
		is_fight_last = Globals.is_fight
	if shooted_bullet >= max(Globals.Enemy_Full_Health, 3):
		high_way.attack("player")
		shooted_bullet = 0
func e_atk():
	if node2d.check_enemy():
		high_way.attack("enemy")
	else:
		shoot_toggle()
		reset_item()

func e_atked():
	shoot_toggle()
	reset_item()

func reset_item():
	for item_index in range(36):
			if inventory.items[item_index+9] is Item:
				inventory.set_item(item_index+9, null)
