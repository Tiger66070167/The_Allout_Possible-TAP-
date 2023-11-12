extends Control


func _unhandled_input(event):
	if event.is_action_pressed("ESC"):
		$"..".visible = false

func _on_CheckButton_toggled(button_pressed):
	OS.window_fullscreen = !OS.window_fullscreen


func _on_exit_pressed():
	$"..".visible = false


func _on_HSlider_value_changed(value):
	set_bus_volume(0, value)

func _on_HSlider2_value_changed(value):
	set_bus_volume(1, value)

func set_bus_volume(bus_index: int, value: float) -> void:
	AudioServer.set_bus_volume_db(bus_index, linear2db(value))
	AudioServer.set_bus_mute(bus_index, value < 0.01)
