extends Control
var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")
func _ready():
	get_tree().paused = false
	
func _process(delta):
	"""Just pause menu"""
	if Input.is_action_just_pressed("ESC"):
			get_tree().paused = not get_tree().paused
			get_node("Pause_menu").visible = not get_node("Pause_menu").visible

func can_drop_data(position, data):
	return data is Dictionary and data.has("item")

func drop_data(position, data):
	inventory.set_item(data.item_index, data.item)
	print(inventory.items[data.item_index].name)
