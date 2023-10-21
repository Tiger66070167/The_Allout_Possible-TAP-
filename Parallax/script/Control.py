from godot import exposed, export
from godot import *


@exposed
class Control(Control):

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		pass
	def _on_Button_pressed(self):
		self.get_tree().quit()
