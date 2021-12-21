#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    load_from_json_file = __import__('6-load_from_\
json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    file_name = "add_item.json"
    new_list = load_from_json_file(file_name)
    i = 0
    while (i < len(sys.argv)):
        if (i == 0):
            save_to_json_file(new_list, file_name)
        else:
            new_list.append(sys.argv[i])
            save_to_json_file(new_list, file_name)
        i += 1
