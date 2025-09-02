# pip/pip3

## Difference between pip and pip3
pip is used to manage packages for Python 2; pip3 is for Python 3

On Pop 22.04, only Python 3 is installed out of the box.
Also, pip and pip3 are linked to the same executable so may be used interchangeably.


## Find packages which have updates available
`pip list --outdated`


## Install package into python instance
`pip install {PACKAGE_NAME}`


## Upgrade an already-installed package
`pip install --upgrade {PACKAGE_NAME}`


## Get details of a package
`pip show {PACKAGE_NAME}`



## Creating a requirements file

In general, can install a list of packages from a 'requirements.txt' file.  However, local packages (i.e. in the repository) cause errors when executing `python -m pip install requirements`.  To avoid, when exporting package list to requirements.txt, include the --exclude-editable flag.
`pip list --format=freeze --exclude-editable`.
Can install these local packages via `pip install -e .`
