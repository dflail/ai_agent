# This function checks if a given directory is within the specified working directory.
# It returns a success message if the directory is valid and an error message if it is not.

import os

from openai import files



def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_work_dir, directory))

        if not os.path.commonpath([abs_work_dir, target_dir]) == abs_work_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        files = os.listdir(target_dir)
        if not files:
            return f'No files found in the directory: "{directory}"'
        return get_user_output(files, target_dir)
    
    except Exception as e:
        return f"Error: {e}"


# This function generates a formatted string containing information about the files in the specified directory.
def get_user_output(list_of_files: list, directory: str) -> str:
    result = f"Result for {directory} directory:\n"
    files = list_of_files

    for file in files:
        result += (f"- {file}: file_size={os.path.getsize(os.path.join(os.path.abspath(directory), file))} bytes, is_dir={os.path.isdir(os.path.join(os.path.abspath(directory), file))}\n")

    return result