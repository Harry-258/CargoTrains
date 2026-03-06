import unittest
from unittest.mock import patch
from src.station import Station
from src.utils import print_graph, read_input


class ReadInputTests(unittest.TestCase):
    @patch("builtins.input")
    @patch("builtins.print")
    def test_read_input_returns_station_with_correct_negative_values(self, mock_print, mock_input):
        """
        The function should handle negative numbers.
        """
        mock_input.side_effect = ["2 1", "1 -20 -30", "-2 -30 40", "1 -2", "1"]

        station = read_input()

        self.assertEqual(station.id, 1)
        self.assertEqual(station.c_unloaded, -20)
        self.assertEqual(station.c_loaded, -30)
        self.assertEqual(len(station.connections), 1)

        station2 = list(station.connections)[0]
        self.assertEqual(station2.id, -2)
        self.assertEqual(station2.c_unloaded, -30)
        self.assertEqual(station2.c_loaded, 40)
        self.assertCountEqual(station2.connections, {})

        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 0)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_read_input_asks_for_input_until_valid(self, mock_print, mock_input):
        """
        The function should ask the user for the input until it gets a valid input.
        """
        inputs = [
            "2 3 4",  # Incorrect input
            "ab iub",  # Incorrect input
            "2.5 3.0",  # Incorrect input
            "2 2",  # Number of stations and tracks
            "1 0 30",  # First station
            "2 5 40",  # Second station
            "1 2",  # First track
            "aaa",  # Incorrect input, start the process again
            "2 2",  # Number of stations and tracks
            "1 100 35",  # First station
            "2 25 49",  # Second station
            "1 2",  # First track
            "2 1",  # Second track
            "2",  # Starting station
        ]
        mock_input.side_effect = inputs

        station = read_input()

        self.assertEqual(station.id, 2)
        self.assertEqual(station.c_unloaded, 25)
        self.assertEqual(station.c_loaded, 49)
        self.assertEqual(len(station.connections), 1)

        station2 = list(station.connections)[0]
        self.assertEqual(station2.id, 1)
        self.assertEqual(station2.c_unloaded, 100)
        self.assertEqual(station2.c_loaded, 35)
        self.assertEqual(len(station2.connections), 1)

        self.assertEqual(mock_input.call_count, len(inputs))
        self.assertEqual(mock_print.call_count, 4)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_read_input_correctly_reads_input(self, mock_print, mock_input):
        """
        The function should correctly read the input from the user and return a Station object.
        """
        mock_input.side_effect = ["2 1", "1 20 30", "2 30 40", "1 2", "1"]

        station = read_input()

        self.assertEqual(station.id, 1)
        self.assertEqual(station.c_unloaded, 20)
        self.assertEqual(station.c_loaded, 30)
        self.assertEqual(len(station.connections), 1)

        station2 = list(station.connections)[0]
        self.assertEqual(station2.id, 2)
        self.assertEqual(station2.c_unloaded, 30)
        self.assertEqual(station2.c_loaded, 40)
        self.assertCountEqual(station2.connections, {})

        self.assertEqual(mock_input.call_count, 5)
        self.assertEqual(mock_print.call_count, 0)

class PrintGraphTests(unittest.TestCase):
    @patch("builtins.print")
    def test_correctly_displays_the_cargo_types(self, mock_print):
        """
        The function should correctly display the cargo types of each station.
        """
        station1 = Station(1, 100, 10)
        station2 = Station(2, 10, 50)
        station3 = Station(3, 5, 30)
        station4 = Station(4, 6, 40)

        station1.add_connection(station2)
        station2.add_connection(station3)
        station3.add_connection(station4)
        station4.add_connection(station2)

        station2.cargo_types = {10, 30, 40, 50}
        station3.cargo_types = {30, 40, 50}
        station4.cargo_types = {30, 40, 50}

        print_graph(station1)

        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call("Station 1: None")
        mock_print.assert_any_call("Station 2: {40, 10, 50, 30}")
        mock_print.assert_any_call("Station 3: {40, 50, 30}")
        mock_print.assert_any_call("Station 4: {40, 50, 30}")

if __name__ == "__main__":
    unittest.main()
