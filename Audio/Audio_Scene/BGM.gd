extends Node

var not_in_battle = load("res://Audio/BGM/Normal Fade in.wav")
var battle = load("res://Audio/BGM/Fighting.wav")
var menu = load("res://Audio/BGM/Main Menu.wav")
	
func main_menu():
	$BGM.stream = menu
	$BGM.play()
	
func play_music_not_in_battle():
	$BGM.stream = not_in_battle
	$BGM.play()

func play_music_in_battle():
	$BGM.stream = battle
	$BGM.play()

func turn_down_volume():
	$BGM.volume_db = -12

func reset_volume():
	$BGM.volume_db = 0


func _on_BGM_finished():
	pass
