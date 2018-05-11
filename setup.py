from setuptools import setup
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='page-counter',
    version='1.0.1',
    packages=['page_counter'],
    url='https://github.com/bircow/page-counter',
    license='MIT',
    author='Libor Jelinek',
    author_email='ljelinek@virtage.com',
    description='Small Python library and commandline tool to count number of standard pages in the text, files and folders. Comes with common standard page dialects but is super easy to bring your own definition.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing'],
    install_requires=['beautifulsoup4'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'page-counter = page_counter.cli:main',
        ]
    }
)
