# function_grapher — GitHub‑Optimized README (Unified Block)

A lightweight command-line tool for graphing mathematical functions using Python and matplotlib.  
function_grapher provides an interactive CLI for visualizing linear, quadratic, and sine functions with user-defined parameters and ranges.

------------------------------------------------------------
FEATURES
------------------------------------------------------------

- Interactive command-line interface
- Supports linear, quadratic, and sine functions
- User-defined x-range and resolution
- Clean matplotlib output
- Modular src/ layout for easy maintenance
- Simple to extend with new function types

------------------------------------------------------------
INSTALLATION
------------------------------------------------------------

Create and activate a virtual environment:

    python -m venv .venv
    .venv\Scripts\activate

Install the package in editable mode:

    pip install -e .

------------------------------------------------------------
USAGE
------------------------------------------------------------

Run the CLI tool:

    function_grapher

Or run the module directly:

    python -m function_grapher.main

You will be prompted to:

- Choose a function type
- Enter x-range values
- Enter function parameters
- View the generated plot

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

function_grapher/
│
├── src/
│   └── function_grapher/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   └── test_basic.py
│
├── pyproject.toml
├── README.md
├── LICENSE
├── CHANGELOG.md
├── requirements.txt
└── Makefile

------------------------------------------------------------
DEVELOPMENT
------------------------------------------------------------

Install development tools:

    pip install pytest ruff build

Run tests:

    pytest

Lint and format:

    ruff check .
    ruff format .

Build the distribution:

    python -m build

------------------------------------------------------------
LICENSE
------------------------------------------------------------

This project is licensed under the MIT License.  
See the LICENSE file for details.

------------------------------------------------------------
CHANGELOG
------------------------------------------------------------

See CHANGELOG.md for version history and release notes.

------------------------------------------------------------
END OF README
------------------------------------------------------------