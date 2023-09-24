extends Node2D
var hp: int = 3
const dam: int = 1
var selectes = false
# Called when the node enters the scene tree for the first time.
func _ready():
	$Player.position = Vector2(200, 200)

func _on_area_2d_input_event(viewport, event, shape_idx):
	if Input.is_action_just_pressed("Left_Mouse"):
		selectes = true
		print("Yes")
		
func _physics_process(delta):
	if selectes:
		global_position = lerp(global_position, get_global_mouse_position(), 25*delta)
		

