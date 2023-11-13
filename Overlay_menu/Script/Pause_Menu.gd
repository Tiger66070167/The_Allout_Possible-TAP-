extends Control


var is_paused = false setget set_is_paused
var high_way = preload("res://Main Scene/resource/new_resource.tres")
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

func _on_option_pressed():
	get_node("/root/Main/option").visible = true
