from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as _build_ext

# Custom build class to ensure proper behavior when calling C++ compiler
class build_ext(_build_ext):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = ['-std=c++17']  # Ensure C++17 standard
        super().build_extensions()

hello_extension = Extension(
    "my_package.libhello",  # Name of the compiled shared library
    sources=["cpp/hello.cpp"],
    include_dirs=["cpp"],  # Add the C++ header directory
    language="c++",
)

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    ext_modules=[hello_extension],
    cmdclass={"build_ext": build_ext},
)
