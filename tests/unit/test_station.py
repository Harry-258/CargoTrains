import unittest

from src.station import Station


class StationTest(unittest.TestCase):
    def test_add_connections(self):
        station = Station(0, 1, 2)

        self.assertEqual(station.connections, [])

        station1 = Station(1, 2, 3)
        station2 = Station(2, 1, 3)
        station.add_connection(station1)
        station.add_connection(station2)

        self.assertCountEqual(station.connections, [station1, station2])


if __name__ == "__main__":
    unittest.main()
