extends Sprite2D


# Called when the node enters the scene tree for the first time.
func _ready():
	print('Player')
	print(Globals.health)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	#Rotation
	#if Input.is_action_pressed("Left_Mouse"):
	#	rotation_degrees += 90*delta
	#HP Test
	if Input.is_action_just_pressed("Space_bar"):
		Globals.health -= 1
		$"../UI".health()

#func _input(event):
#	if event.is_action_released(""):
#		$".".position = Vector2(300, 300)



