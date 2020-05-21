from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylinebot',
    packages=['pylinebot'],

    version='1.0.1',

    license='Apache License 2.0',

    install_requires=['line-bot-sdk', 'pillow'],

    author='nanato12',
    author_email='admin@nanato12.info',

    url='https://github.com/nanato12/pylinebot',

    description='linebot-sdk-python wrapper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='linebot linebot-sdk linebot-sdk-python-wrapper',

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
