# pyautoall

Tool for automatically generating `__all__` assignments
in `__init__.py` files.

## Installation

Install the tool

```shell
  cd autoall
  pip install .
```

## Usage

```
usage: AutoAll [-h] [-i] [-c] filepath

Automatically generate __all__. Uses AST parser to identify all imports and automatically create a `__all__` variable

positional arguments:
  filepath       The filepath to generate __all__ for.

options:
  -h, --help     show this help message and exit
  -i, --inplace  (default: False) If set, will automatically update the file
  -c, --concise  (default: False) If set, will only print the __all__ statement for copying and pasting the file manually. Overrides -i, --inplace
```

## Adding autoall to PyCharm

