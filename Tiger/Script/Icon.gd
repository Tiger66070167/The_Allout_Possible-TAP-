extends Sprite2D
var pos: Vector2 = Vector2.ZERO
const speed: int = 100
# Called when the node enters the scene tree for the first time.
func _ready():
	pos = Vector2(100, 100)
	position = pos


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pos.x += speed*delta
	rotation_degrees += 100*delta
	position = pos
	
	Input
