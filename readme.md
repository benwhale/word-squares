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

It has been written in Python 3.9.5 but should run with a python version > 3.4

## Installation

Uses a virtualenv to manage dependencies

Create and activate a venv

then run pip install -r requirements.txt to install project requirements.

Finally run pip install -e . to install the cli command word-squares into this virtual environment in development mode.


Developed in Python 3.9.5, definitely requires Python > 3.4

## Usage

I've gone with a two stage approach, where we index a dictionary first, and then use that to solve in a seperate command 

Ensure you have indexed first with command ```word-squares index-data```
This will prompt you to provide the file location of the dictionary. It can alternatively be passed in with the -f flag
``` word-squares index-data -f enable1.txt```

Once indexed, you can then proceed to run the solver with the command
`word-squares solve 4 eeeeddoonnnsssrv`- replacing 4 and the word string with the desired dimension/letters

## Testing

Unit tests have been written using Pytest. word_squares/tests/test_demo.py contains each of the examples given.
The third example has more than one solution, and the program discovers an alternative solution first.
I have included a slight hack to allow either solution in the unit test for completion, although in its current form
the application is predictable so will not produce the result. Removing the cast to list from set in the solve method
would allow either to be returned, as sets are unordered, but it would be at the expense of the predictability elsewhere.


## Formatting
This project has been formatted using black, and linted using flake8 ( a wrapper for PEP8 and some other useful tools)

```black .```

```flake8 .```

Known issues which would have been addressed if more time

- Currently creates a log file wherever you run it from. Could do with setting this up properly with a config file
- Test case with two answers - could be an extension to store successful solutions and then only return when the whole combination of options had been explored
- We could do something smarter to identify if we are placing a middle diagonal letter and cut out some letter iterations in the process
  (we should only use letters with more than one letter of that character if not a diagonal)
- Data access layer for DAWG library, and maybe for the numpy array
- Failing better when data hasn't been preindexed
- build/deployment didn't quite work, would have been nice to get that working so it doesn't need installing in development mode.
- requirements.txt needs pruning, as the whole scipy stack has been installed. This could be reduced to just the requirements of numpy.
- sphinx install to build / render documentation from docstrings
- tests