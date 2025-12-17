from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy as np
import os

USE_OPENMP = os.environ.get("USE_OPENMP", False)
print("USE_OPENMP", USE_OPENMP)

extra_compile_args = ["-fopenmp"] if USE_OPENMP else []
extra_link_args = ["-fopenmp"] if USE_OPENMP else []

extensions = [
    Extension(
        "ssm.cstats",
        sources=["ssm/cstats.pyx"],
        language="c++",
        include_dirs=[np.get_include()],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3"},
    )
)
