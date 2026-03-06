from collections import deque
from src.station import Station


def read_input():
	"""
	Reads input from the terminal to construct a graph of stations with directed edges as tracks.
	If the input is invalid, the function will ask the user to try again until the input is valid.
	:return: A Station object representing the starting station.
	"""
	while True:
		try:
			station_number, track_number = map(int, input("Please enter the number of stations followed by the number of tracks: ").split())

			stations = {}
			for index in range(station_number):
				station_id, c_unloaded, c_loaded = map(int, input(f"Enter the station ID, the cargo it unloads, and the cargo type it loads for station {index + 1}/{station_number}: ").split())
				stations[station_id] = Station(station_id, c_unloaded, c_loaded)

			for _ in range(track_number):
				track_from, track_to = map(int, input("Enter the IDs of the stations where a track should leave from and go to: ").split())
				stations[track_from].add_connection(stations[track_to])

			starting_station = int(input("Enter the ID of the starting station: "))

			return stations[starting_station]
		except ValueError:
			print("Invalid input. Please ensure you type the correct number of integers separated by spaces.\n")
		except KeyError:
			print("Invalid input. Please try again, only building tracks between station IDs that exist.\n")

def print_graph(station: Station):
	"""
	Prints the cargo types for each station.
	:param station: The starting station.
	"""
	visited = set()
	visited.add(station)
	queue = deque([station])

	while queue:
		current_station = queue.popleft()
		print(f"Station {current_station.id}: {'None' if len(current_station.cargo_types) == 0 else current_station.cargo_types}")
		for connected_station in current_station.connections:
			if connected_station not in visited:
				visited.add(connected_station)
				queue.append(connected_station)