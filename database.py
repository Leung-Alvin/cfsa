import os
import shutil

# TODO:
# - Use SQLite instead of a custom implementation

# helper directory operations - CLI
def get_folders_in_directory(directory_path):
    folders = [
        f
        for f in os.listdir(directory_path)
        if os.path.isdir(os.path.join(directory_path, f))
    ]
    return folders


def get_files_in_folder(folder_path):
    files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]
    return files


def get_valid_input(prompt, lower_bound, upper_bound):
    while True:
        try:
            user_input = int(input(prompt))
            if lower_bound <= user_input <= upper_bound:
                return user_input
            else:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Please enter a valid integer.")


def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")


# Special directory operations
def get_authors(directory):
    authors = []
    for filename in os.listdir(directory):
        author = filename.split("_-_")[0]
        if author not in authors:
            authors.append(author)
    return authors


def add_database(directory_path):
    try:
        default_folder = "databases"

        directory_path = os.path.join(default_folder, directory_path)
        os.makedirs(directory_path)
        print(f"Directory '{directory_path} created successfuly.")
    except OSError as e:
        print(f"Failed to create directory '{directory_path}': {e}")


def add_print(new_file_name, new_content, folder):
    base_directory = "databases"
    folders = get_folders_in_directory(base_directory)

    # for i, subdirectory in enumerate(folders, 1):
    # print(f"{i}. {subdirectory}")

    # selected_folder_index = get_valid_input("Enter the number of the folder you want to edit: ", 1, len(folders))
    selected_folder = os.path.join(base_directory, folder)
    # selected_folder = os.path.join(base_directory, folders)
    # new_file_name = input("Enter the name of the new print: ")
    # new_content = input("Enter the content for the new print (Press Enter if none):\n")

    new_file_path = os.path.join(selected_folder, new_file_name)

    with open(new_file_path, "w") as new_file:
        new_file.write(new_content)

    # print(f"\nFile '{new_file_name}' has been added to '{selected_folder}'.")


def edit_print(file_name, folder):
    base_directory = "databases"
    folders = get_folders_in_directory(base_directory)

    # print("Select a folder: ")
    # for i, folder in enumerate(folders, 1):
    # print(f"{i}, {folder}")
    # selected_folder_index = get_valid_input("Enter the number of the folder you want to edit: ", 1, len(folders))
    selected_folder = os.path.join(base_directory, folder)

    files_in_selected_folder = get_files_in_folder(selected_folder)

    # print(f"\nFiles in '{selected_folder}':")
    # for i, file in enumerate(files_in_selected_folder, 1):
    # print(f"{i}. {file}")

    # selected_file_index = get_valid_input("Enter the number of the print you want to edit: ", 1, len(files_in_selected_folder))
    # selected_file = os.path.join(selected_folder, files_in_selected_folder[selected_file_index - 1])
    selected_file = os.path.join(selected_folder, files_in_selected_folder)

    with open(selected_file, "r") as file:
        current_content = file.read()

    print(f"\nCurrent content of '{selected_file}':\n{current_content}")

    action = get_yes_no_input(
        "Do you want to delete or add content to the file? (yes/no): "
    )

    if action == "yes":
        substring_to_delete = input("Enter the substring to delete from the file:\n")
        updated_content = current_content.replace(substring_to_delete, "")
        print(
            f"\nSubstring '{substring_to_delete}' has been deleted from '{selected_file}'."
        )
    else:
        new_content = input("Enter the new content to add to the file:\n")
        updated_content = current_content + " " + new_content + "\n"
        print(f"\nNew content has been added to '{selected_file}'.")

    with open(selected_file, "w") as file:
        file.write(updated_content)

    print(f"\nFile '{selected_file} has been updated.")


# def copy_prints(file_path):


def remove_strings_with_substring(input_list, substring):
    updated_list = [string for string in input_list if substring not in string]
    return updated_list


def get_databases():
    dirs = [x[0] for x in os.walk("databases")]
    ret = remove_strings_with_substring(dirs, ".git")
    ret.remove("databases")
    new_ret = []
    for db in ret:
        new_ret.append(db.replace(".\\", ""))
    return new_ret


def get_prints(directory):
    prints = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            prints.append(filename)
    return prints


def read_print(directory, print_name):
    with open(directory + "/" + print_name, "r") as f:
        return f.read()


def main():
    dbs = get_databases()
    for db in dbs:
        authors = get_authors(db)
        # prints = get_prints(db)
        # print(db, authors, prints)
        print(db, authors)


if __name__ == "__main__":
    main()
