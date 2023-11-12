extends Control


var is_paused = false setget set_is_paused

func _unhandled_input(event):
	if event.is_action_pressed("ESC"):
		self.is_paused = !is_paused


func set_is_paused(value):
	is_paused = value
	get_tree().paused = is_paused
	visible = is_paused

func _on_Resume_Game_pressed():
	self.is_paused = false
	visible = is_paused

func _on_Quit_pressed():
	self.is_paused = false
	get_tree().quit()

func _on_Reset_Game_pressed():
	pass
