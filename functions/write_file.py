import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file relative to the working directory. Creates parent directories if they do not exist and overwrites existing files.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path of the file to write to, relative to the working directory.",
                },
                "content": {
                    "type": "string",
                    "description": "The full text content to write into the file.",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abspath: str = os.path.abspath(working_directory)
        target_file = os.path.normpath(
            os.path.join(working_dir_abspath, file_path))
        if os.path.commonpath([working_dir_abspath, target_file]) != working_dir_abspath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(target_file)
        os.makedirs(parent_dir, exist_ok=True)
        with open (target_file, mode="w") as f:
            f.write(content)
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as err:
        return f"Error encountered \nError: {err}"
