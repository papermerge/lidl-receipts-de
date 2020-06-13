from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="lidl-recepts-de",
    version="0.1.0",
    author="Eugen Ciur",
    author_email="eugen@papermerge.com",
    url="https://github.com/papermerge/lidl-receipts-de",
    description="Metadata plugin for lidl receipts (used in Germany)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0 License",
    keywords="metadata, papermerge, plugin, receipts",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
