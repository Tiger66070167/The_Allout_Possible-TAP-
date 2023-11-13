extends Control

onready var wave_label = get_node("CenterContainer/HBoxContainer/Wave")
func _ready():
	pass # Replace with function body.
	
func _process(_delta):
	wave_label.set_text("Enemy Left : "+str(len(Globals.enemy_wave)-1))
 
