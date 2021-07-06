# Word Squares Solver

This repository contains my solution to a 'word square' generation problem. The dimension of the square and characters
to populate it are provided, and the application will attempt to fill a square grid with valid words which read
the same both horizontally and vertically such as below

```
rose
oven
send
ends
```

It has been written in Python 3.9.5, and I would recommend running it with an up to date version of python3
but should run with a python version > 3.4

## Installation

I recommend using a venv virtual environment to install into.

To create a virtual environment you can use the following commands:

* UNIX based systems:

        python3 -m venv venv

* Windows based systems:

        py -3 -m venv venv

Once you have created the virtual environment you can activate it by running the following:

* UNIX based systems:

        . venv/bin/activate

* Windows based systems:

        venv\Scripts\activate


Once your venv is activated, run 

        pip install -r requirements.txt

to install project requirements.
On a windows machine it may request the installation of Microsoft Visual C++ 14.0 or greater. This is in order to build the underlying DAWG data structure.

Finally run

        pip install -e .

to install the cli command word-squares into this virtual environment in development mode.

## Usage

I've gone with a two stage approach, where we index a dictionary first, and then use that to solve in a seperate command 

The cli is built using the click library, and inline help can be viewed using the `--help` flag.

Ensure you have indexed the dictionary first with command

        word-squares index-data

This will prompt you to provide the file location of the dictionary. It can alternatively be passed in with the -f flag

        word-squares index-data -f enable1.txt

Once indexed, you can then proceed to run the solver with the command

        word-squares solve 4 eeeeddoonnnsssrv

replacing 4 and the word string with the desired dimension/letters

## Testing

Some unit tests have been written using Pytest. word_squares/tests/test_demo.py contains each of the examples given.
The third example has more than one solution, and the program discovers an alternative solution first.
I have included a slight hack to allow either solution in the unit test for completion, although in its current form
the application is predictable so will not produce the result. Removing the cast to list from set in the solve method
would allow either to be returned, as sets are unordered, but it would be at the expense of the predictability elsewhere.

I had limited time to finish off writing the tests I would ideally have written for the application. I have created
empty test methods with comments explaining what I would have written for reference & as a discussion point.

## Formatting
This project has been formatted using black, and linted using flake8 (a wrapper for pycodestyle and some other useful tools)

Format python files with the command

        black .

Check for linting issues with the command

        flake8

## Extensions and Known issues
(in note form for discussion)

- Test case with two answers - could be an extension command option to store successful solutions and then only return when the whole combination of options had been explored
- We could do something smarter to identify if we are placing a middle diagonal letter and cut out some letter iterations in the process
  (we should only use letters with more than one letter of that character if not a diagonal)
- Data access layer for DAWG library, and potentially abstraction of the numpy array to allow easy change of storage
- Failing better when data hasn't been preindexed
- Build/deployment didn't quite work in time, would have been nice to get that working so it doesn't need installing in development mode.
- The requirements.txt needs pruning, as much of the scipy stack has been installed. This should be reduced to just the requirements of numpy.
- Method comments are present - this could be built with Sphinx to render readthedocs style documentation from docstrings
- More unit tests given more time
