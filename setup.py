from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-alarm',
    version='0.0.1',
    description='A test python radio alarm clock.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jubbathejack/python-alarm-clock',
    license='MPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MPL License',
        'Programming Language :: Python :: 3'
    ],
    scripts=["bin/python-alarm"],
    python_requires='>=3.5'
)
