#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = ["hello", 2, (3, 6), 4, 5]

nb_print = safe_print_list(my_list, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) - 1)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 10)
print("nb_print: {:d}".format(nb_print))
