extends CenterContainer

onready var itemTextureRect = $ItemTextureRect

func display_item(item):
	if item is Item:
		itemTextureRect.set_texture(item.get_texture())
	else:
		pass
