import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="tull",
    version="0.1",
    scripts=["tull"],
    author="Lokendra Sharma",
    author_email="lokendra.sharma.one@gmail.com",
    description="tull helps you tull",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/l0k3ndr/tull",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
