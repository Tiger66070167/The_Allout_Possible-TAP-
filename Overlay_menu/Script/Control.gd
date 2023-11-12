extends Control

var open = false setget set_is_open

func _unhandled_input(event):
	if event.is_action_pressed("ESC"):
		self.open = false


func set_is_open(value):
	open = value
	visible = open


func _on_CheckButton_toggled(button_pressed):
	OS.window_fullscreen = !OS.window_fullscreen
