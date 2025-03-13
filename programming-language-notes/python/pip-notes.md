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
