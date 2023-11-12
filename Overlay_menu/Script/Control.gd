extends Control


func _unhandled_input(event):
	if event.is_action_pressed("ESC"):
		$"..".visible = false

func _on_CheckButton_toggled(button_pressed):
	OS.window_fullscreen = !OS.window_fullscreen


func _on_exit_pressed():
	$"..".visible = false
