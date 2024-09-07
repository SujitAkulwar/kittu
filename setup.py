setup(
    name='kittu',
    version='0.1',
    py_modules=['kittu'],
    install_requires=[
        'psutil', 
    ],
    entry_points={
        'console_scripts': [
            'kittu = kittu:main', 
        ],
    },
    author='Sujit Akulwar',
    author_email='sujitakulwar@gmail.com', 
    description='A CLI tool for recording PC stats',
)