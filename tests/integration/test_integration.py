import unittest
from unittest.mock import patch

from src.algorithms import find_cargo_types
from src.utils import read_input, print_graph


class IntegrationTests(unittest.TestCase):
    @patch("builtins.input")
    @patch("builtins.print")
    def test_utils_and_algorithms(self, mock_print, mock_input):
        """
        The functions in utils and algorithms should work together correctly.
        """
        inputs = [
            "4 4",
            "1 0 10",
            "2 10 20",
            "3 5 30",
            "4 6 40",
            "1 2",
            "2 3",
            "3 4",
            "4 2",
            "1"
        ]
        mock_input.side_effect = inputs

        station = read_input()
        find_cargo_types(station)
        print_graph(station)

        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_input.call_count, len(inputs))

        mock_print.assert_any_call("Station 1: None")
        mock_print.assert_any_call("Station 2: [10, 20, 30, 40]")
        mock_print.assert_any_call("Station 3: [20, 30, 40]")
        mock_print.assert_any_call("Station 4: [20, 30, 40]")

if __name__ == "__main__":
    unittest.main()
