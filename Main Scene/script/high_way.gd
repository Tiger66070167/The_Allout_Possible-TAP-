extends Resource
class_name High_way

signal set()
signal reset()
signal shoot()

signal player_atk()
signal player_atked()
signal enemy_atk()
signal enemy_atked()

signal p_anim_done(damage)
signal n_anim_done(damage)

signal get_enemy_left()
var my_yield = 0

func get_enemy_left():
	emit_signal("get_enemy_left")

func get_enemy_hp():
	return Globals.Enemy_Full_Health

func just_set():
	emit_signal("set")

func just_reset():
	emit_signal("reset")

func just_shoot():
	emit_signal("shoot")
	
func attack(entity):
	if entity == "player":
		emit_signal("player_atk")
	else:
		emit_signal("enemy_atk")
func get_my_yield():
	return my_yield

func attacked(entity):
	if entity == "player":
		my_yield +=1
		if my_yield >= 2:
			my_yield = 0
			emit_signal("player_atked")
	else:
		my_yield +=1
		if my_yield >= 2:
			my_yield = 0
			emit_signal("enemy_atked")
