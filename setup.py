"""Python setup.py for nba_stats package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("nba_stats", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="nba_stats",
    version=read("nba_stats", "VERSION"),
    description="Awesome nba_stats created by JDSanti",
    url="https://github.com/JDSanti/NBA-Stats/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="JDSanti",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["nba_stats = nba_stats.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
