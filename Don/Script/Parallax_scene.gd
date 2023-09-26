extends Node2D
# Called when the node enters the scene tree for the first time.
var toggle = true
func _ready():
	get_tree().paused = false


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_just_pressed("ESC"):
		get_tree().paused = not get_tree().paused
		$Pause_Menu.visible = not $Pause_Menu.visible

func _on_button_button_down():
	if toggle == true:
		$Upper_scene/Player/Player_animate.play("Running")
		Globals.screen_move_x = 40
		toggle = false
	else:
		$Upper_scene/Player/Player_animate.play("Idle")
		Globals.screen_move_x = 0
		toggle = true
