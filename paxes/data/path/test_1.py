from . import path
import os

def test():
    answer = path(os.path.join("pdb", "3j5p.pdb"))
    here = os.path.dirname(os.path.realpath(__file__))
    expected = os.path.join(
        here,
        "..",
        "raw",
        "pdb",
        "3j5p.pdb",
    )
    assert answer == expected
