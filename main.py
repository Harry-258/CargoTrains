from src.algorithms import find_cargo_types
from src.utils import read_input, print_graph

if __name__ == '__main__':
	station = read_input()
	find_cargo_types(station)
	print_graph(station)