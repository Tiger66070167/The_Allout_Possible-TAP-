extends TextureRect

@export var type: InventoryItems.Type

func set_size_icon(i: InventoryItems.Type, cms: Vector2) -> void:
	type = i
	custom_minimum_size = cms

#still broken
func _can_drop_data(at_position: Vector2, data:Variant) -> bool:
	if data is InventoryItems:
		if type == InventoryItems.Type.Empty:
			if get_child_count() == 0:
				return true
			else:
				return false
		else:
			return data.type == type
	return false

func _drop_data(at_position: Vector2, data: Variant) -> void:
	if get_child_count() > 0:
		var item := get_child(0)
		remove_child(item)
		data.get_parent().add_child(item)
	data.get_parent().remove_child(data)
	add_child(data)
