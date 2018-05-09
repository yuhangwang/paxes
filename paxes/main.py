"""
Calculate the principal axes for selected atoms.

Example input specifications (YAML style):
outputs:
    out.h5
inputs:
    my.psf
    my.pdb
    my.dcd
params:
    selections:
    - chain A and resid 547 to 598
    - chain B and resid 547 to 598
    - chain C and resid 547 to 598
"""

from paxes import inertia

def main(specs: dict):
    print()

if __name__ == '__main__':
    main(specs: dict)
