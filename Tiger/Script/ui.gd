extends CanvasLayer

@onready var health_ui: TextureProgressBar = $Health/TextureProgressBar

func health():
	health_ui.value = Globals.health

