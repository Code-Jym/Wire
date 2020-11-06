from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Python_Wire",
    version = "1.1",
    author = "Tomi Adenekan",
    author_email = "adenekanoluwatomison2024@serrahs.com",
    description = ("Strings, But Better"),
    license = "MIT",
    keywords = "strings",
    url = "https://github.com/Code-Jym/wire",
    long_description = read("README.md"),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Strings",
        "License :: OSI Approved :: MIT License"
    ]
)
