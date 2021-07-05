from setuptools import setup

setup(
    name="word_squares",
    version="0.1.0",
    packages=["word_squares"],
    include_package_data=True,
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "word-squares = word_squares.cli.app:cli",
        ]
    },
)
