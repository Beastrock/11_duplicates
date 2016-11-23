import os


def get_all_files_info(*paths):
    return [(name, os.path.getsize(os.path.join(folder, name)), os.path.join(folder, name))
            for path in paths
            for folder, sub_folders, file_names in os.walk(path)
            for name in file_names]


def get_duplicates(files_info):
    file_name_and_file_path_dict = {}
    for file_name, file_size, file_path in files_info:
        file_name_and_file_path_dict.setdefault(file_name, [])
        file_name_and_file_path_dict[file_name].append(file_path)
    for file_name, file_paths in file_name_and_file_path_dict.items():
        if len(file_paths) < 1:
            del [file_name]
    return file_name_and_file_path_dict


def print_duplicates(duplicates_dict):
    if not duplicates_dict:
        print("Duplicates have not been found")
        return
    for duplicate_name, duplicates_paths in duplicates_dict.items():
        print("\nDuplicates of {} have been found in:".format(duplicate_name))
        for duplicates_path in duplicates_paths:
            print("{}".format(duplicates_path))


if __name__ == "__main__":
    folder = input("Input desired folder path:\n")
    optional_folder = input("Input one more folder path or press ENTER to continue:\n")
    all_files = get_all_files_info(folder, optional_folder)
    print_duplicates(get_duplicates(all_files))
