extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
func _ready():
	pass # Replace with function body.

func _process(delta):
	var enemy_anim = get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim/")
	var player_anim = get_node("Player_anim")
	if str(player_anim.get_animation()) == "Attack" and player_anim.get_frame() in [1, 6]:
		enemy_anim.play("Damaged")
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed

func _on_Player_anim_animation_finished():
	var player_anim = get_node("Player_anim")
	if str(player_anim.get_animation()) == "Damaged":
		player_anim.play("Idle")
	if str(player_anim.get_animation()) == "Attack":
		player_anim.play("Running")
		get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()