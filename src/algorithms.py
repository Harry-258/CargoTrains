from collections import deque
from src.station import Station


def find_cargo_types(station: Station):
	"""
	Finds the cargo types that a train can arrive with at each station. Saves the cargo types in the station object.
	:param station: The starting station.
	"""
	queue = deque([station])

	while len(queue) > 0:
		current_station = queue.popleft()

		# Use the cargo types from the current station after cargo has been loaded/unloaded.
		outgoing_cargo_types = set(current_station.cargo_types)
		outgoing_cargo_types.discard(current_station.c_unloaded)
		outgoing_cargo_types.add(current_station.c_loaded)

		for connected_station in current_station.connections:
			# Add the station to the queue if there are new cargo types.
			new_cargo = outgoing_cargo_types - connected_station.cargo_types
			if new_cargo:
				connected_station.cargo_types.update(new_cargo)

				if connected_station not in queue:
					queue.append(connected_station)