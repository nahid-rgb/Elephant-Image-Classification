from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

# Type hint: str means file_path should be a string.
# Return type: List[str]
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of required libraries.
    """
    requirements = []

    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements


setup(
    name="elephant_classification",
    version="0.0.1",
    author="Mahfujur Rahman",
    author_email="rmahfuzur818@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt")
)



"""
WHAT IS setup.py:
A configuration file that makes our elephant_classification project
an installable Python package.

WHY WE NEED IT:
So we can import our own project modules from different files
without worrying about the current working directory.

KEY FUNCTIONS:
- get_requirements(): Reads requirements.txt and removes "-e ."
  because it is not an actual Python library.
- find_packages(): Finds all Python packages inside the src folder
  (folders containing __init__.py).
- setup(): Registers our project as an editable Python package
  along with its dependencies.

HOW IT WORKS:
When we run `pip install -r requirements.txt`, pip encounters "-e ."
and installs our local project in editable mode using setup.py.

This allows changes in our source code to be available without
reinstalling the package.
"""