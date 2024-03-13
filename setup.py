from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='This package sorts a given array and returns the top n elements in descending order',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/SundayKelechi/my_first_py_package',
    author='Sunday Kelechi',
    author_email='sundaykc3@gmail.com'
)