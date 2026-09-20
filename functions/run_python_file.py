import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its execution status, STDOUT, and STDERR.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the Python file (.py) to execute, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional list of command-line arguments to pass to the Python script.",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
        working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abspath: str = os.path.abspath(working_directory)
        target_file = os.path.normpath(
            os.path.join(working_dir_abspath, file_path))
        target_file_parentdir = os.path.dirname(target_file)
        if os.path.commonpath([working_dir_abspath, target_file]) != working_dir_abspath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file]
        if args != None:
            command.extend(args)
        sp = subprocess.run(command, capture_output=True, cwd=target_file_parentdir, timeout=30, text=True)
        return_string = ""
        if sp.returncode != 0:
            return_string += f"Process exited with code {sp.returncode}."
        if sp.stderr == "" and sp.stdout == "":
            return_string += " No output produced."
        return_string += f"STDOUT: {sp.stdout}STDERR: {sp.stderr}"
        return return_string
    except Exception as err:
        return f"Error encountered \nError: {err}"
    