from pkg_resources import parse_requirements
from setuptools import find_packages, setup


__author__ = 'Sanz009'


with open("requirements.txt") as f:
    REQUIREMENTS = [str(req) for req in parse_requirements(f.read())]

setup(
    name="dictcompare",
    version="1.0.0",
    install_requires=REQUIREMENTS,
    description="Deep Dict Compare",
    packages=find_packages(exclude=["tests", "tests.*"])
)

