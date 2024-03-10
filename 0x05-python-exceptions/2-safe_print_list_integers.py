#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for counter in range(0,x):
        try:
            print("{:d}".format(my_list(counter)), end="")
        except (TypeError, ValueError):
            continue
        counter += 1
    print("")
    return (counter)
