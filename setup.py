from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='belka',
    version='0.5.0',
    description='Simple currency converter for BYN',
    long_description=readme,
    author='OfficerKoo',
    author_email='charmakesthingsawesome@gmail.com',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=['urllib3'],
    entry_points={
        'console_scripts': [
            'belka=belka.cli:main',
            ]
    }
)