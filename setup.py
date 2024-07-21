from setuptools import setup, find_packages

setup(
    name="shiv_cli",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'click',
        'colorama'  # Need for ANSI on Windows
    ],
    entry_points={
        'console_scripts': [
            'shiv_cli=shiv_cli.cli:main',
        ],
    },
)
