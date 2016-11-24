import os


def get_duplicates(*paths):
    files_info = {}
    for path in paths:
        for folder_name, sub_folders, file_names in os.walk(path):
            for file_name in file_names:
                file_path = os.path.join(folder_name, file_name)
                file_size = os.path.getsize(os.path.join(folder_name, file_name))
                file_name_and_size = "{}:{}".format(file_name, file_size)
                files_info.setdefault(file_name_and_size, [])
                files_info[file_name_and_size].append(file_path)
    if not [value for value in files_info.values() if len(value) > 1]:
        return None
    else:
        return {key: value for key, value in files_info.items() if len(value) > 1}


def print_duplicates(duplicates):
    if not duplicates:
        print("Duplicates have not been found")
        return
    for file_name_and_size, file_paths in duplicates.items():
        file_name = file_name_and_size.split(":")[0]
        print("\nDuplicates of \"{}\" have been found in:".format(file_name))
        for file_path in file_paths:
            print(file_path)


if __name__ == "__main__":
    folder = input("Input desired folder path:\n")
    optional_folder = input("Input one more folder path or press ENTER to continue:\n")
    all_files = get_duplicates(folder, optional_folder)
    print_duplicates(all_files)
