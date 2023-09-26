extends TextureRect
class_name Items

enum Type {Chip, Empty}
@export var type:Type

func get_iteam(small_icon:Type, how_like:Texture2D) -> void:
	type = small_icon
	texture = how_like
	expand_mode = TextureRect.EXPAND_FIT_WIDTH_PROPORTIONAL
	stretch_mode = TextureRect.STRETCH_KEEP_ASPECT

func _get_drag_data(at_position:Vector2) -> Variant:
	set_drag_preview(drop_iteam())
	return self

func drop_iteam() -> TextureRect:
	var set_icon := TextureRect.new()
	set_icon.texture = texture
	set_icon.expand_mode = TextureRect.EXPAND_IGNORE_SIZE
	set_icon.stretch_mode = TextureRect.STRETCH_KEEP_ASPECT_CENTERED
	set_icon.custom_minimum_size = size
	return set_icon
	
	


