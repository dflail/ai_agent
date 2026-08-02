# This function checks if a given directory is within the specified working directory.
# It returns a success message if the directory is valid and an error message if it is not.

import os



def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_work_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_work_dir, directory))

        if not os.path.commonpath([abs_work_dir, target_dir]) == abs_work_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        return f'Success: "{directory}" is within the working directory'
    
    except Exception as e:
        return f"Error: {e}"