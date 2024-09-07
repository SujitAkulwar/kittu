from setuptools import setup, find_packages

setup(
    name='kittu',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'kittu=kittu:main',
        ],
    },
    author='Sujit Akulwar',
    author_email='sujitakulwar@gmail.com',
    description='A command-line tool for recording PC stats using psutil.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sujitakulwar/kittu',
)
