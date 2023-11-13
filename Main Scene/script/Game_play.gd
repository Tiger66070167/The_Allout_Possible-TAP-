extends Control

onready var le_py = get_node("CanvasLayer/Inventory_contianer/le_py")

func _on_Reset_button_pressed():
	le_py.random_item()
