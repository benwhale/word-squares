# Word Squares Solver

## Installation

Uses a virtualenv to manage dependencies

Create and activate a venv

then run pip install -r requirements.txt

Python > 3.4



## Usage

Either install locally using setup.py 

Ensure you have indexed first with command [1]




## Formatting
This project has been formatted using black, and linted using flake8 ( a wrapper for Pep8 and some other useful tools)

```black .```

```flake8 .```

Known issues which would have been addressed if more time

- Currently creates a log file wherever you run it from. Could do with setting this up properly with a config file
- Test case with two answers - could be an extension to store successful solutions and then only return when the whole combination of options had been explored
- We could do something smarter to identify if we are placing a middle diagonal letter and cut out some letter iterations in the process
  (we should only use letters with more than one letter of that character if not a diagonal)
- Data access layer
