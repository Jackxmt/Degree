from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="Degree",
    version="1.0.2",
    description="a new type for variable in Python - Degree",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url
    author="Jackxmt",
    # author_email
    # classifiers=[]
    # keywords
    # package_dir
    packages=find_packages(where="src"),
    python_requires=">=3, <4"
    # ...
)

