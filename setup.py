# from distutils.core import setup
from setuptools import setup
from Cython.Build import cythonize
from setuptools_rust import RustExtension, Binding

setup(
    name="paxes",
    version="0.1.0",
    license="MIT/X11",
    author="Yuhang (Steven) Wang",
    author_email="stevenyhw.project@gmail.com",
    packages=[
        "paxes",
        "paxes.inertia",
        "paxes.hello",
        "paxes.inertia_tensor",
    ],
    package_data={
        "paxes": ["paxes/*/*.pxd"],
    },
    ext_modules=cythonize("**/*.pyx"),
    rust_extensions=[
        RustExtension("paxes.inertia_tensor._inertia_tensor",
            "paxes/rs_inertia_tensor/Cargo.toml",
            binding=Binding.RustCPython),
    ],
    install_requires=[
        "ProDy",
        "cytoolz",
        "atomicblock",
        "numpy",
    ],
)
