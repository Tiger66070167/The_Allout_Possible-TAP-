extends Label

func _process(_delta):
	set_text("Kill Count: "+str(Globals.kill_count))
	get_node("/root/Main/Parallax_scene/Lower_scene/Control_panel/Reset_count").set_text("Item Reset Count: "+str(Globals.reset_count))
