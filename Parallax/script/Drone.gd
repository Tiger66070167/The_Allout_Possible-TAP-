extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
onready var drone_anim = get_node("Drone_anim")
onready	var player_anim = get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
onready var energy_gun_1 = $Energy_gun1
onready var energy_gun_2 = $Energy_gun2
onready var get_hit = $get_hit

var high_way = preload("res://Main Scene/resource/new_resource.tres")

func _ready():
	high_way.just_set()

func _process(delta):
	if str(drone_anim.get_animation()) == "Attack":
		if drone_anim.get_frame() in [8, 13]:
			if drone_anim.get_frame() in [8]:
				energy_gun_1.play()
			elif drone_anim.get_frame() in [13]:
				energy_gun_2.play()
			player_anim.play("Damaged")
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed

func _on_Drone_anim_animation_finished():
	if str(drone_anim.get_animation()) == "Death":
		Globals.kill_count += 1
		queue_free()
	elif str(drone_anim.get_animation()) == "Attack":
		drone_anim.play("Running")
		get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()
	elif str(drone_anim.get_animation()) == "Damaged":
		Globals.Enemy_Health -= Globals.Player_damage
		get_hit.play()
		drone_anim.play("Idle")
