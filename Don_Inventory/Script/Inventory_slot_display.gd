extends CenterContainer

var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")
onready var slot = $Slot

func display_item(item):
	if item is Item:
		slot.set_texture(item.texture)
		slot.rect_min_size = Vector2(0, 0)
		slot.rect_scale = Vector2(3, 3)
	else:
		slot.rect_scale = Vector2(1, 1)
		slot.rect_min_size = Vector2(180, 180)
		slot.texture = load("res://Don_Inventory/Asset/EmptyInventorySlot_SMALLEST_clear.png")

func get_drag_data(_position):
	var item_index = get_index()
	var item = inventory.remove_item(item_index)
	if item is Item:
		var data = {}
		data.item = item
		data.item_index = item_index
		var darg_preview = TextureRect.new()
		darg_preview.texture = item.texture
		set_drag_preview(darg_preview)
		return data

func can_drop_data(_position, data):
	return data is Dictionary and data.has("item")

func drop_data(_position, data):
	var my_item_index = get_index()
	var _my_item = inventory.items[my_item_index]
	inventory.swap_items(my_item_index, data.item_index)
	inventory.set_item(my_item_index, data.item)
