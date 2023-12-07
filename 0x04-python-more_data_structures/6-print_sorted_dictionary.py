#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = {}
    for key, value in sorted(a_dictionary.items()):
        sorted_dict[key] = value
        print("{}: {}".format(key, value))
