import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="tull",
    version="0.6",
    scripts=["tull"],
    author="Lokendra Sharma",
    author_email="lokendra.sharma.one@gmail.com",
    description="tull helps you to Teleport Ur Logs with Love",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/l0k3ndr/tull",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click==8.0.1",
        "itsdangerous==2.0.1",
        "Jinja2==3.0.1",
        "MarkupSafe==2.0.1",
        "requests==2.26.0",
        "Werkzeug==2.0.1",
        "Flask==2.0.1",
        "bleach==3.3.0",
        "certifi==2021.5.30",
        "charset-normalizer==2.0.1",
        "colorama==0.4.4",
        "docutils==0.17.1",
        "idna==3.2",
        "importlib-metadata==4.6.1",
        "keyring==23.0.1",
        "packaging==21.0",
        "pkginfo==1.7.1",
        "Pygments==2.9.0",
        "pyparsing==2.4.7",
        "readme-renderer==29.0",
        "requests==2.26.0",
        "requests-toolbelt==0.9.1",
        "rfc3986==1.5.0",
        "six==1.16.0",
        "tqdm==4.61.2",
        "twine==3.4.1",
        "urllib3==1.26.6",
        "webencodings==0.5.1",
        "zipp==3.5.0"
    ]
)
