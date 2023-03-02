from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Store Application'
LONG_DESCRIPTION = 'Simple application to test synergies between pandas and sqlite'

# Setting up
setup(
    name="StorApp",
    version=VERSION,
    author="Bogdan Fometescu",
    author_email="<mbogdan.fometescu@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python', 'dataframe', 'pandas'],
    url="https://github.com/BogdanMFometescu/StoreApp",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
