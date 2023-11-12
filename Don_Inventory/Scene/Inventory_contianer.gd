extends Control

var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")
var item_path_list = {
		"gold":preload("res://Don_Inventory/Resource/gold.tres"), 
		"gun":preload("res://Don_Inventory/Resource/gun.tres"), 
		"stone":preload("res://Don_Inventory/Resource/stone.tres"), 
		"tree":preload("res://Don_Inventory/Resource/tree.tres"), 
	}
func _ready():
	pass
func can_drop_data(_position, data):
	return data is Dictionary and data.has("item")

func drop_data(_position, data):
	inventory.set_item(data.item_index, data.item)
	print(inventory.items[data.item_index].name)
func set_item_but_for_python(item_index, item):
	inventory.set_item(item_index, item_path_list[item])
