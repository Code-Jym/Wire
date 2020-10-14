import setuptools
from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))

with open(path.join(f"{this_directory}", 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="SWire",
    packages=setuptools.find_packages(),
    version="0.1",
    license="MIT",
    description="Python Strings But Better",
    long_description=long_description,
    author="Tomi Adenekan",
    author_email="adenekanoluwatomison2024@serrahs.com",
    url="https://github.com/Code-Jym/wire",
    download_url="https://github.com/Code-Jym/wire/archive/v_01.tar.gz",
    keywords=["strings", "python", "reimplementation"],
    install_requires = [],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ]
)