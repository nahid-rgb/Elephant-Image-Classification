
import os
import sys
import yaml
import json

from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from elephant_classification.logging.logger import logging
from elephant_classification.exception.exception import ElephantClassificationException


# 1. Read YAML file and return its contents as ConfigBox
@ensure_annotations  # Checks function arguments against their type hints at runtime and raises an error if the types don't match.
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents.

    ConfigBox allows us to access dictionary values
    using dot notation.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            logging.info(f"YAML file loaded successfully: {path_to_yaml}")

            return ConfigBox(content)

    except Exception as e:
        raise ElephantClassificationException(e, sys)


# 2. Create multiple directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create a list of directories if they do not already exist.
    """
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)

            if verbose:
                logging.info(f"Directory created: {path}")

    except Exception as e:
        raise ElephantClassificationException(e, sys)


# 3. Save data in JSON format
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save dictionary data into a JSON file.
    """
    try:
        # Create parent directory if it does not exist
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as file:
            json.dump(data, file, indent=4)

        logging.info(f"JSON file saved: {path}")

    except Exception as e:
        raise ElephantClassificationException(e, sys)


# 4. Load data from JSON file
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load JSON data and return it as ConfigBox.
    """
    try:
        with open(path, "r") as file:
            content = json.load(file)

        logging.info(f"JSON file loaded: {path}")

        return ConfigBox(content)

    except Exception as e:
        raise ElephantClassificationException(e, sys)


# 5. Write data into a YAML file
@ensure_annotations
def write_yaml_file(file_path: Path, content: dict, replace: bool = False):
    """
    Write dictionary data into a YAML file.

    If replace=True, overwrite the existing file.
    """
    try:
        if replace and file_path.exists():
            file_path.unlink()

        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w") as file:
            yaml.safe_dump(content, file, sort_keys=False)

        logging.info(f"YAML file saved: {file_path}")

    except Exception as e:
        raise ElephantClassificationException(e, sys)


# 6. Get file size in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024)

        return f"~ {size_in_kb} KB"

    except Exception as e:
        raise ElephantClassificationException(e, sys)
