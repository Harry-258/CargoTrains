class Station:
	def __init__(self, station_id, c_unloaded, c_loaded):
		self.id = station_id
		self.c_unloaded = c_unloaded
		self.c_loaded = c_loaded
		self.connections = []
		self.cargo_types = []

	def add_connection(self, station):
		self.connections.append(station)