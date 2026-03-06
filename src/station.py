class Station:
	def __init__(self, station_id, c_unloaded, c_loaded):
		self.id = station_id
		self.c_unloaded = c_unloaded
		self.c_loaded = c_loaded
		self.connections = set()
		self.cargo_types = set()

	def add_connection(self, station):
		self.connections.add(station)