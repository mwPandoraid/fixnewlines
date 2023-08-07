low quality tool for fixing newline issues

usage: `fixnewlines.py ./`

this program works recursively by default, checking and modifying every file in the directory tree

you can add ignored extensions to the ignored_extensions list in the source code

features:
- makes sure file doesnt start with a newline
- makes sure file ends with a newline
- makes sure file doesnt end with trailing newlines

note: the -r (--recursive) flag is nonfunctional as of now, this tool only works in recursive mode.

warning: this program modifies file contents - make sure to have a backup just in case
