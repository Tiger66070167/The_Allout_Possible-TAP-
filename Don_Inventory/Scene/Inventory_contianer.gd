extends Control

var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")
var item_path_list = {
		"UPPER":preload("res://Don_Inventory/Resource/UPPER.tres"), 
		"RIGHT":preload("res://Don_Inventory/Resource/RIGHT.tres"), 
		"LEFT":preload("res://Don_Inventory/Resource/LEFT.tres"), 
		"DOWN":preload("res://Don_Inventory/Resource/DOWN.tres"), 
	}
func _ready():
	pass
func can_drop_data(_position, data):
	return data is Dictionary and data.has("item")

func drop_data(_position, data):
	inventory.set_item(data.item_index, data.item)
func set_item_but_for_python(item_index, item):
	inventory.set_item(item_index, item_path_list[item])
