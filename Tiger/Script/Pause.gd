extends Control



func _unhandled_input(event):
	if event.is_action_pressed("ESC"):
		self.is_paused = !is_paused


var is_paused = false:
	set(value):
		is_paused = value
		get_tree().paused = is_paused
		visible = is_paused


func _on_button_1_pressed():
	self.is_paused = false


func _on_quit_pressed():
	get_tree().quit()
