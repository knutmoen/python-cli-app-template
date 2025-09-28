from setuptools import setup, find_packages

setup(
    name="mycli-app",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mycli=mycli.cli:main",
        ],
    },
    install_requires=[],
)
