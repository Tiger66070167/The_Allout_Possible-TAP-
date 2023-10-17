extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
onready var drone_anim = get_node("Drone_anim")
onready	var player_anim = get_node("/root/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
func _ready():
	pass # Replace with function body.

func _process(delta):
	if str(drone_anim.get_animation()) == "Attack" and drone_anim.get_frame() == 8:
		player_anim.play("Damaged")
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed


func _on_Drone_anim_animation_finished():
	if str(drone_anim.get_animation()) == "Death":
		get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()
		queue_free()
	elif str(drone_anim.get_animation()) == "Attack":
		drone_anim.play("Running")
		get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()
	elif str(drone_anim.get_animation()) == "Damaged":
		drone_anim.play("Idle")
