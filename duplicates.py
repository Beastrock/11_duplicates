import os
import sys


def get_duplicates_dictionary_list(*paths):
    files = []
    for path in paths:
        for folder_name, sub_folders, file_names in os.walk(path):
            for file_name in file_names:
                file_path = os.path.join(folder_name, file_name)
                file_size = os.path.getsize(file_path)
                if (file_name, file_size) in files:
                    '''
                    dupl_path - path of the first from two duplicates,is named
                     like this because of the short recommended string length
                    '''
                    dupl_path = files[files.index((file_name, file_size)) - 1]
                    yield {file_name: (file_path, dupl_path)}
                files.append(file_path)
                files.append((file_name, file_size))


def print_duplicates(duplicates_dictionary_list):
    for duplicates_dictionary in duplicates_dictionary_list:
        for name, paths in duplicates_dictionary.items():
            print("Duplicates of {} have been found in directories:"
                  "\n{}\n{}".format(name, paths[0], paths[1]))
    return


if __name__ == "__main__":
    duplicates_dictionary_list = get_duplicates_dictionary_list(sys.argv[1:])
    print_duplicates(duplicates_dictionary_list)
