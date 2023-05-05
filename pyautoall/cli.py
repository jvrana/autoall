"""
comment
import something


"""
# import something
import argparse
import ast
from builtins import open, classmethod
from os.path import abspath
from typing import Optional

parser = argparse.ArgumentParser(
                    prog='AutoAll',
                    description='Automatically generate __all__. Uses AST parser to identify all imports and '
                                'automatically create a `__all__` variable',
                    epilog='')
parser.add_argument('filepath', help="The filepath to generate __all__ for.")
parser.add_argument('-i', '--inplace',
                    action='store_true', help="(default: False) If set, will automatically update the file")
parser.add_argument('-c', '--concise',
                    action='store_true', help="(default: False) If set, will only print the __all__ statement for "
                                              "copying and pasting the file manually. Overrides -i, --inplace")


def main():
    args = parser.parse_args()
    filepath = args.filepath
    inplace = args.inplace
    concise = args.concise

    collected_all = []
    with open(filepath, 'r') as f:
        txt = f.read()
        tree = ast.parse(txt)

        all_stmt: Optional[ast.Assign] = None
        for stmt in tree.body:
            if isinstance(stmt, ast.Assign):
                try:
                    _id = stmt.targets[0].id
                    if _id == '__all__':
                        all_stmt = stmt
                        break
                except Exception:
                    ... # ignore errors here
        for stmt in tree.body:
            if isinstance(stmt, (ast.Import, ast.ImportFrom)):
                for _import in stmt.names:
                    name = _import.name
                    if name not in collected_all:
                        collected_all.append(name)

    new_all_stmt = "# autogenerated by autoall\n"
    new_all_stmt += "__all__ = [\n"
    for x in collected_all:
        new_all_stmt += "    \'" + x + "\',\n"
    new_all_stmt += "]\n\n"

    needs_change = True
    if all_stmt:
        if set(collected_all) == set([x.value for x in all_stmt.value.elts]):
            needs_change = False

    if needs_change:
        if concise:
            print(abspath(filepath))
            print(new_all_stmt)
        else:
            with open(filepath, 'r') as f:
                lines = f.readlines()
            if all_stmt:
                lineno = all_stmt.lineno - 1
                for i in range(lineno, all_stmt.end_lineno):
                    lines.pop(lineno)
                lines.insert(lineno, new_all_stmt)
            else:
                lines.append(new_all_stmt)

            updated_txt = ''.join(lines)
            if inplace:
                print(filepath)
                with open(filepath, 'w') as f:
                    f.write(updated_txt)
            else:
                print(updated_txt)

    else:
        if concise:
            ...
        else:
            print(f"No changes needed for {filepath}")


