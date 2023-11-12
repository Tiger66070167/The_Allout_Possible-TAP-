extends GridContainer


var inventory = preload("res://Don_Inventory/Resource/Inventory.tres")

func _ready():
	inventory.connect("item_changed", self, "_on_item_changed")
	update_inventory_display()

func _process(_delta):
	update_inventory_display()
	
func update_inventory_display():
	for item_index in inventory.items.size():
		update_inventory_slot_display(item_index)
		
func update_inventory_slot_display(item_index):
	var item_slot = get_child(item_index)
	var item = inventory.items[item_index]
	item_slot.display_item(item)
	
func _on_item_changed(indexes):
	for item_index in indexes:
		update_inventory_slot_display(item_index)
