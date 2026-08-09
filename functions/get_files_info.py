# This code defines a function `get_files_info` that checks if a given directory is within a specified working
# directory and returns information about the files in that directory. 
# It also includes a helper function `get_formatted_output` that formats the output of the file information.

import os

from openai import files


# This function generates a formatted string containing information about the files in the specified directory.
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
        return get_formatted_output(files, target_dir)
    
    except Exception as e:
        return f"Error: {e}"


# This helper function formats the output of the file information, including file size and whether it is a directory.
def get_formatted_output(list_of_files: list, directory: str) -> str:
    result = f"Result for {directory} directory:\n"
    files = list_of_files

    for file in files:
        result += (
            f"- {file}: file_size={os.path.getsize(os.path.join(os.path.abspath(directory), file))} bytes, "
            f"is_dir={os.path.isdir(os.path.join(os.path.abspath(directory), file))}\n"
        )

    return result