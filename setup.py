from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.open()

setup(
    name='belka',
    version='0.4.20',
    description='Simple currency converter for BYN',
    long_description=readme,
    author='OfficerKoo',
    author_email='charmakesthingsawesome@gmail.com',
    packages=find_packages('src'),
    packages_dir={'':'src'},
    install_requires=[]
)