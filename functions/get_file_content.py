import os

from get_files_info import get_files_info

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abspath: str = os.path.abspath(working_directory)
        target_file = os.path.normpath(
            os.path.join(working_dir_abspath, file_path))
        if os.path.commonpath([working_dir_abspath, target_file]) != working_dir_abspath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content
    except Exception as err:
        return f"Error encountered \nError: {err}"
