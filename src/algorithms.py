from station import Station


def find_cargo_types(station: Station):
	"""
	Finds the cargo types that a train can arrive with at each station. Saves the cargo types in the station object.
	:param station: The starting station.
	"""

	queue = [station]
	visited = set(station.id)

	while len(queue) > 0:
		current_station = queue.pop(0)

		# Use the cargo types from the current station after cargo has been loaded/unloaded.
		cargo_types = current_station.cargo_types
		cargo_types.append(current_station.c_loaded)
		cargo_types.pop(current_station.c_unloaded)

		for connected_station in current_station.connections:
			if connected_station.id not in visited:
				visited.add(connected_station.id)
				queue.append(connected_station)

			for cargo_type in cargo_types:
				if cargo_type not in connected_station.cargo_types:
					connected_station.cargo_types.append(cargo_type)