extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
onready var hammer_anim = get_node("Hammer_anim")
onready	var player_anim = get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene/Player/Player_anim")
onready var hammer_hit_sound = $Hit
onready var hammer_charge_sound = $Charge
onready var beam_sound = $Beam

var high_way = preload("res://Main Scene/resource/new_resource.tres")

func _ready():
	high_way.just_set()

func _process(delta):
	if str(hammer_anim.get_animation()) == "Attack":
		if hammer_anim.get_frame() in [0]:
			hammer_charge_sound.play()
		if hammer_anim.get_frame() in [6, 14]:
			if hammer_anim.get_frame() in [6]:
				hammer_hit_sound.play()
			elif hammer_anim.get_frame() in [14]:
				beam_sound.play()
			player_anim.play("Damaged")
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed

func _on_Hammer_anim_animation_finished():
	if str(hammer_anim.get_animation()) == "Death":
		Globals.kill_count += 1
		queue_free()
	elif str(hammer_anim.get_animation()) == "Attack":
		hammer_anim.play("Running")
		get_node("/root/Main/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()
	elif str(hammer_anim.get_animation()) == "Damaged":
		Globals.Enemy_Health -= Globals.Player_damage
		hammer_anim.play("Idle")
