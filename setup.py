"""
PHAST forcefields
"""
from setuptools import setup
import versioneer

short_description = __doc__.split("\n")

try:
    with open("README.md") as file:
        long_description = file.read()
except IOError:
    long_description = "\n".join(short_description[2:])

setup(
    name="phastforcefields",
    description=short_description[0],
    long_description=long_description,
    author="Adam Hogan",
    url="https://github.com/space-group-research/phast-forcefields",
    include_package_data=True,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license="MIT",
    packages=["phastforcefields", "phastforcefields.tests"],
    package_data={"phastforcefields": ["offxml/*"]},
    entry_points={
        "openforcefield.smirnoff_forcefield_directory": [
            "get_forcefield_dirs_paths = phastforcefields.phastforcefields:get_forcefield_paths"
        ]
    },
    zip_safe=True

)
