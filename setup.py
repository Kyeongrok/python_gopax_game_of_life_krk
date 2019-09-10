from setuptools import setup
from gameoflife.game import __version__

setup(
    name='gameoflife_krk',
    version=__version__,
    author='kyeongrok',
    author_email='oceanfog1@gmail.com',
    packages=['gameoflife'],
    include_package_data=True,
    description='conway_s gameoflife of life',
    license='bsd',
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python"
    ],
    entry_points={
        'console_scripts': [
            'run_gameoflife=gameoflife.game:main',
        ]
    }
)
