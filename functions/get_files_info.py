import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abspath: str = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abspath, directory))
        if os.path.commonpath([working_dir_abspath, target_dir]) != working_dir_abspath:
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        # return f"Success: \"{directory}\" is within the working directory"
        dir_contents = get_dir_contents(target_dir)
        rstr: str = ""
        for file in dir_contents:
            rstr += f"  - {file["name"]}: file_size={file["size"]} bytes, is_dir={file["is_dir"]}\n"
        return rstr
    except Exception as err:  # noqa: BLE001
        return f"Error encountered \nError: {err}"


def get_dir_contents(dir_abspath: str) -> list[dict[str, int | bool | str]]:
    dir_members = os.listdir(dir_abspath)
    def to_element_info(file): return file_info(
        os.path.join(dir_abspath, file))
    dir_info = list(map(to_element_info, dir_members))
    return dir_info

    # return list(filter(lambda element: not isdir(element), dir_members_absp))


def file_info(file_abs_path: str) -> dict[str, int | bool | str]:

    return {
        "name": os.path.basename(file_abs_path),
        "size": os.path.getsize(file_abs_path),
        "is_dir": os.path.isdir(file_abs_path)
    }

