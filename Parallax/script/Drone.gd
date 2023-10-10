extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
func _ready():
	pass # Replace with function body.

func _process(delta):
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed


func _on_Drone_anim_animation_finished():
	var dron_anim = get_node("Drone_anim")
	if str(dron_anim.get_animation()) == "Death":
		queue_free()

func _on_Effect_animation_finished():
	var effect = get_node("Effect")
	if str(effect.get_animation())  == "Gun_Hit":
		effect.play("Nope")
