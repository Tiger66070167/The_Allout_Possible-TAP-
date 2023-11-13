extends Node

#parallax scene value
onready var Player_Health = 5
onready var Player_damage = 1

onready var Enemy_Health = 0
onready var Enemy_Full_Health = 0
onready var Enemy_damage = 1

onready var game_state = ""
onready var enemy_wave = ["null"]
onready var diffculty = 0.5

onready var game_wave = 0

onready var is_fight = false

onready var shoot = false
onready var just_set = false

onready var is_shoot = false

var kill_count = 0
var reset_count = 0
