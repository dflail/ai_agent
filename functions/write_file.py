# This is a utility function to write content to a file within a specified working directory.

import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_work_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_work_dir, file_path))

        if not os.path.commonpath([abs_work_dir, abs_file_path]) == abs_work_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure the directory exists
        print(f"DEBUGGING: {os.path.dirname(abs_file_path)}")
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(abs_file_path, 'w') as file:
            file.write(content)
        
        if os.path.isdir(abs_file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"