import os


def get_duplicates_dictionaries_list(*paths):
    files = []  # the list structure is [file_path, (file_name, size), ...]
    duplicates_in_folder = False
    for path in paths:
        for folder_name, sub_folders, file_names in os.walk(path):
            for file_name in file_names:
                file_path = os.path.join(folder_name, file_name)
                file_size = os.path.getsize(file_path)
                if (file_name, file_size) in files:
                    # dupl_path - path of the first from two duplicates, which
                    # is already in list. Named shortly for str length < 79.
                    dupl_path = files[files.index((file_name, file_size)) - 1]
                    yield {file_name: (file_path, dupl_path)}
                    duplicates_in_folder = True
                files.append(file_path)
                files.append((file_name, file_size))
    if not duplicates_in_folder:
        yield None


def print_duplicates(duplicates_dictionaries_list):
    of_the_first_file = 0
    of_the_second_file = 1
    for duplicates_dictionary in duplicates_dictionaries_list:
        if not duplicates_dictionary:
            print("Duplicates have not been found")
            return
        for name, path in duplicates_dictionary.items():
            print("\nDuplicates of {} have been found in:\n{}\n{}".format
                  (name, path[of_the_first_file], path[of_the_second_file]))
    return


if __name__ == "__main__":
    folder_path = input("Input desired folder path:\n")
    optional_folder_path = input(
        "Input another folder path or type enter to continue:\n")
    duplicates_dictionary_list = get_duplicates_dictionaries_list(
        folder_path, optional_folder_path)
    print_duplicates(duplicates_dictionary_list)
