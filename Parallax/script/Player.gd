extends KinematicBody2D
# Called when the node enters the scene tree for the first time.
onready var Target_pos = position
onready var SPEED = 200
func _ready():
	pass # Replace with function body.

func _process(delta):
	var player_anim = get_node("Player_anim")
	var enemy_path = {"Drone":"/root/Parallax_scene/Upper_scene/Fighting_scene/Drone/Drone_anim/", \
		"Ball_guy":"/root/Parallax_scene/Upper_scene/Fighting_scene/Ball_guy/Ball_anim/", \
		"Hammer_dude":"/root/Parallax_scene/Upper_scene/Fighting_scene/Hammer_dude/Hammer_anim/"}
	if get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").get_child_count() == 2:
		var enemy_anim = ""
		if len(Globals.enemy_wave) > 1:
			enemy_anim = get_node(enemy_path[Globals.enemy_wave[0]])
		if str(player_anim.get_animation()) == "Attack" and player_anim.get_frame() in [1, 6]:
			enemy_anim.play("Damaged")
		if Globals.Player_Health <= 0:
			player_anim.play("Death")
	position = position.move_toward(Target_pos, SPEED*delta)

func move_to_position(to_position, with_speed=200):
	Target_pos = to_position
	SPEED = with_speed

func _on_Player_anim_animation_finished():
	var player_anim = get_node("Player_anim")
	if str(player_anim.get_animation()) == "Damaged":
		player_anim.play("Idle")
	if str(player_anim.get_animation()) == "Death":
		get_node("/root/Parallax_scene/Death_menu").visible = true
	if str(player_anim.get_animation()) == "Attack":
		Globals.Enemy_Health -= 5
		player_anim.play("Running")
		get_node("/root/Parallax_scene/Upper_scene/Fighting_scene").is_done_toggle()
