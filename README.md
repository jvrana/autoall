# pyautoall

Tool for automatically generating `__all__` assignments
in `__init__.py` files. You can add it to PyCharm to automatically generate `__all__` from imported located in the `__init__` file (uses AST parsing). Thats it. It might save you a few minutes a day. Enjoy.

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
  -i, --inplace  (default: False) If set, will automatically update the file.
  -c, --concise  (default: False) If set, will only print the __all__ statement for copying and pasting the file manually. Overrides -i, --inplace
```

## Adding autoall to PyCharm

After installation, get the absolute path of pyautoall by running:

```shell
which pyautoall
```
![Alt text](pycharm_external_tools.png "PyCharm External Tools Settings")




