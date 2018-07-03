import os
from hedwig.core import settings
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='hedwig',
    version=settings.VERSION,
    packages=["hedwig"],
    include_package_data=True,
    license='MIT License',
    description=settings.DESCRIPTION,
    long_description=README,
    url='https://github.com/skblaz/hedwig2',
    author='Blaz Skrlj',
    author_email='blaz.skrlj@ijs.si',
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
)
