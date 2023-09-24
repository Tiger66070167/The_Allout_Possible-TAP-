extends Node2D

var DIR = OS.get_executable_path().get_base_dir()
var interpreter = DIR.path_join("Python/virtual_environment/Scripts/python.exe")
var pyscript = DIR.path_join("Python/virtual_environment/Scripts/helloword.py")

# Called when the node enters the scene tree for the first time.
func _ready():
	if !OS.has_feature("standalone"):
		interpreter = ProjectSettings.globalize_path("res://Python/virtual_environment/Scripts/python.exe")
		pyscript = ProjectSettings.globalize_path("res://Python/virtual_environment/Scripts/helloword.py")
	var test_result = Array()
	var test_process = OS.execute(interpreter, [pyscript, "helloman"], test_result, true)
	test_result = str(test_result[0]).split(":")
	var result = []
	for i in range(len(test_result)):
		print(test_result[i])
		if str(test_result[i]).is_valid_int():
			result.append(int(test_result[i]))
	print(result)

