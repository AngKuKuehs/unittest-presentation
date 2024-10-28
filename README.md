# Python's unittest Library

Part of Python's standard library

Can be used as a test driver to run all the tests in the python standard library `python -m unittest discover test -v`

It is a clean and minimal yet sufficient testing framework that provides flexibilty.

Features:
- Test cases
- Test fixtures
- Test runner
- Stubs (through `unittest.mock`)

Shortened URL: https://tinyurl.com/py-unittest 

# Set-Up
Clone the repository:
```bash
git clone git@github.com:AngKuKuehs/unittest-presentation.git
```

Create virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the flask API locally:
```bash
flask run
```

# Running Tests
```bash
python -m unittest discover tests -v
```

# Credits
Parts of the repository is adapted from https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Unit-Testing

unittest documentation: https://docs.python.org/3/library/unittest.html 
