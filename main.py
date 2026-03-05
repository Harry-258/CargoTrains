if __name__ == '__main__':
	station_number, track_number = map(int, input().split())

	stations = {}
	for _ in range(station_number):
		station_id, c_unloaded, c_loaded = map(int, input().split())
		stations[station_id] = [c_loaded, c_unloaded]

	tracks = {}
	for _ in range(track_number):
		track_from, track_to = map(int, input().split())

		if track_from not in tracks:
			tracks[track_from] = [track_to]
		else:
			tracks[track_from].append(track_to)

	starting_station = int(input())