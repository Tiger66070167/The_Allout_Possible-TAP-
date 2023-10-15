extends Node2D

var item1 = load("res://Inventory/Item/Item.tscn")
var item2 = load("res://Inventory/Item/Item2.tscn")
var spawn_item = item2.instance()

func _ready():
	$FUCk.add_child(spawn_item)
