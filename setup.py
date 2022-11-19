from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='tcw',
    version='0.0.1',
    author='J Leary',
    author_email='potnanny@gmail.com',
    description='tiny contest winners application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-wtf',
        'sqlalchemy',
        'markdown',
    ],
    entry_points = {
        'console_scripts': [
            'tcwinners=tcw.jobs:main',
        ],
    },
)
