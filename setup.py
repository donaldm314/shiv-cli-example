from setuptools import setup, find_packages

setup(
    name="my_cli_app",
    version="0.1.0",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_cli_app=my_cli_app.cli:main',
        ],
    },
)
