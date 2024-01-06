from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="huflit_api",
    packages=[
        "huflit_api",
        "huflit_api.constants",
        "huflit_api.utils",
        "huflit_api.types",
    ],
    version="0.1a",
    license="gpl-3.0",
    description="I hate the HUFLIT web portal, so I'm making this API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Foxeiz",
    author_email="57582539+FoxeiZ@users.noreply.github.com",
    url="https://github.com/FoxeiZ/huflit_api",
    download_url="https://github.com/FoxeiZ/huflit_api/archive/v0.1.tar.gz",
    keywords=["api", "scraper", "bs4", "huflit"],
    install_requires=[
        "httpx",
        "beautifulsoup4",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  # Again, pick a license
        "Programming Language :: Python :: 3.11",
    ],
)
