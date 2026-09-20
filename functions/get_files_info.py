import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
         working_dir_abspath: str = os.path.abspath(working_directory)
         target_dir_abspath: str = os.path.normpath(os.path.join(
             working_dir_abspath, directory))

         if os.path.commonpath(working_dir_abspath, target_dir_abspath) != working_dir_abspath: # type: ignore
             return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
         if not os.path.isdir(directory):
             return f'Error: "{directory}" is not a directory'
         else:
             return f"Success: \"{directory}\" is within the working directory"
    except Exception as err:  # noqa: BLE001
        return f"Error encountered \nError: {err}"
