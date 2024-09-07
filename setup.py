from setuptools import setup, find_packages

setup(
    name='kittu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['psutil'], 
    entry_points={
        'console_scripts': [
            'kittu=kittu.kittu:main',
        ],
    },
    author='Sujit Akulwar',
    author_email='sujitakulwar@gmail.com',
    description='A CLI tool for recording PC stats',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/kittu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
