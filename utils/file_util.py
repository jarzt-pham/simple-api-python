import os
import json

def read_json(file_path: str):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
        return
    except json.JSONDecodeError:
        print("Invalid JSON")
        return

def make_file_path(file_name: str, folder_paths: str):
    return os.path.join(folder_paths, file_name)
