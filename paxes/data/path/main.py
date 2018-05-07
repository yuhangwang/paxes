import os
"""
Provide absolute path to requested files
"""
def path(file: str) -> str:
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "..",
        "raw",
        file
    )
