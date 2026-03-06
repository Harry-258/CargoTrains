import unittest

from src.algorithms import find_cargo_types
from src.station import Station

class AlgorithmsTests(unittest.TestCase):
    def test_find_cargo_types_one_station(self):
        """
        Since there is only one station, the cargo types should be empty.
        """
        station = Station(0, 1, 2)
        find_cargo_types(station)

        self.assertCountEqual(station.cargo_types, {})

    def test_find_cargo_types_one_station_cycle(self):
        """
        If there is only one station connected to itself, the first station
        should have the cargo type it loads.
        """
        station = Station(0, 0, 1)
        station.add_connection(station)
        find_cargo_types(station)

        self.assertCountEqual(station.cargo_types, {1})

    def test_find_cargo_types_two_stations(self):
        """
        The start station shouldn't have any cargo types. The second station should have
        the cargo type 2 from the cargo loaded in the first station.
        """
        station1 = Station(0, 1, 2)
        station2 = Station(1, 2, 3)
        station1.add_connection(station2)

        find_cargo_types(station1)

        self.assertCountEqual(station2.cargo_types, {2})
        self.assertCountEqual(station1.cargo_types, {})

    def test_find_cargo_types_with_unloading(self):
        """
        The algorithm should handle unloading cargo at a station.
        """
        station1 = Station(0, 1, 2)
        station2 = Station(1, 2, 3)
        station3 = Station(2, 3, 4)
        station1.add_connection(station2)
        station2.add_connection(station3)

        find_cargo_types(station1)

        self.assertCountEqual(station1.cargo_types, {})
        self.assertCountEqual(station2.cargo_types, {2})
        self.assertCountEqual(station3.cargo_types, {3})

    def test_find_cargo_types_with_stations_with_same_cargo_type(self):
        """
        Stations should unload all the cargo of a type they are supposed to unload.
        """
        station1 = Station(0, 0, 2)
        station2 = Station(1, 0, 2)
        station3 = Station(2, 2, 4)
        station4 = Station(3, 5, 6)
        station1.add_connection(station2)
        station2.add_connection(station3)
        station3.add_connection(station4)

        find_cargo_types(station1)

        self.assertCountEqual(station1.cargo_types, {})
        self.assertCountEqual(station2.cargo_types, {2})
        self.assertCountEqual(station3.cargo_types, {2})
        self.assertCountEqual(station4.cargo_types, {4})

    def test_find_cargo_types_cycle(self):
        """
        If there is a cycle in the graph, the stations inside the cycle should have all
        cargo types inside the loop except for the ones that are unloaded.
        """
        station1 = Station(1, 0, 10)
        station2 = Station(2, 10, 20)
        station3 = Station(3, 5, 30)
        station4 = Station(4, 6, 40)

        station1.add_connection(station2)
        station2.add_connection(station3)
        station3.add_connection(station4)
        station4.add_connection(station2)

        find_cargo_types(station1)

        self.assertCountEqual(station1.cargo_types, {})
        self.assertCountEqual(station2.cargo_types, {10, 20, 30, 40})
        self.assertCountEqual(station3.cargo_types, {20, 30, 40})
        self.assertCountEqual(station4.cargo_types, {20, 30, 40})

if __name__ == "__main__":
    unittest.main()
