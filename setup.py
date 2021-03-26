from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="dotenv_manager",
    version=VERSION,
    description="Manager environment variables for different environments",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="environment dotenv manager dev development web",
    url="https://github.com/danilocgsilva/dotenv_manager",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["dotenv_manager"],
    entry_points={"console_scripts": ["demanager=dotenv_manager.__main__:main"],},
    include_package_data=True
)

