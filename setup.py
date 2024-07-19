from setuptools import setup, find_packages

setup(
    name="shiv-cli_example",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'shiv_cli_example=shiv_cli_example.cli:main',
        ],
    },
)
