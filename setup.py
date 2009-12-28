"""
Setup script for the very basic hello world plugin.

Every app should have one!

from the command line run: 'python setup.py develop' and start Gaphor.

A 'Hello world' button should appear in the Help menu. When pressed, a
dialog will be displayed.

Very neat, very... Hello world!
"""


from setuptools import setup, find_packages


setup(
    name = "gaphor.plugins.helloworld",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['gaphor>=0.11.0'],

    namespace_packages = ['gaphor.plugins'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "Arjan Molenaar",
    author_email = "gaphor@gmail.com",
    description = "Example (Hello World) service/plugin for Gaphor",
    license = "GPL",
    keywords = "gaphor hello world example examples",

    entry_points = {
        'gaphor.services': [
            'helloworld = gaphor.plugins.helloworld:HelloWorldPlugin',
        ]
    }
)

# vim:sw=4:et:ai
