from src.station import Station


def read_input():
	f"""
	Reads input from the terminal to construct a graph of stations with directed edges as tracks.
	:return: a {Station} object representing the starting station.
	"""
	station_number, track_number = map(int, input().split())

	stations = {}
	for _ in range(station_number):
		station_id, c_unloaded, c_loaded = map(int, input().split())
		stations[station_id] = Station(station_id, c_unloaded, c_loaded)

	for _ in range(track_number):
		track_from, track_to = map(int, input().split())
		stations[track_from].add_connection(stations[track_to])

	starting_station = int(input())

	return stations[starting_station]

def print_graph(station: Station):
	"""
	Prints the cargo types for each station.
	:param station: The starting station.
	"""
	pass