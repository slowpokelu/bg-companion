from setuptools import find_packages, setup

setup(
    name='bg-companion',
    packages=['src'],
    version='0.1',
    description='The ultimate boardgame companion',
    author='slowpokelu',
    url='https://github.com/slowpokelu/bg-companion',
    entry_points={
        'console_scripts': [
            'companion = main',
        ],
    },
    install_requires=[
        'python-chess',
    ],
)