extends Node

#parallax scene value
onready var Player_Health = 5
onready var Enemy_Health = 0

onready var game_state = "Running"
onready var enemy_wave = ["null"]

onready var game_wave = 0
func _ready():
	pass

func new_wave():
	var enemy_list = ["Drone", "Ball_guy", "Hammer_dude"]
	var rng = RandomNumberGenerator.new()
	rng.seed = hash("I HATE MATH")
	for _i in range(round(3+game_wave/3)):
		enemy_wave.insert(0, enemy_list[rng.randi_range(0, len(enemy_list))])
