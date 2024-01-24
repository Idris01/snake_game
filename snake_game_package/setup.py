from setuptools import setup, find_packages

setup(
    name='snake-game',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'tkinter', 
    ],
    entry_points={
        'console_scripts': [
            'snake-game = snake_game.snake_game:main',
        ],
    },
)
