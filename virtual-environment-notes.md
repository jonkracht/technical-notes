# Virtual environments
Maintain project-specific environments so as to avoid version conflicts



## Background

Works by appending virtual environment files (shims?) to the beginning of the `$PATH` so that executables in the virtual environment are found before those elsewhere in the system

Some tools for managing virtual environments
* `virtualenv`, `virtualenvwrapper`
* [pyenv](https://github.com/pyenv/pyenv)
* `venv`




## virtualenv

[Explanation of virtualenv and Jupyter notebooks](https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415)

### Create a virtual environment

`virtualenv --python=[PYTHON_VERSION] [ENV_NAME]`

### Activate environment  
`source [ENV_NAME]/bin/activate`

### Deactivate environment
`deactivate`

### Add packages to environment
`pip install [PACKAGE_NAME]`  

Include `=={PACKAGE_VERSION}` to specify version


Install all packages listed in a text file:  

`pip install -r {LIST_OF_PACKAGES.txt}`




### Get information about an environment's contents
Use pip/pip3 commands (list, freeze, show)

### Save environment packages to a text file
`pip freeze > [PACKAGE_LIST.txt]`

### Delete an environment
Simply delete the folder in which the environment environment files are stored.  For example, `rm -rf NEW_ENV`




## pyenv

## venv


## Using virtual environments in a Jupyter notebook

Must have the IPython kernel installed
Do so by `pip install ipykernel`

Activate virtual environment


Add virtual environment to IPython
`python -m ipykernel install --user --name=[ENV_NAME]`


List available environments
`jupyter kernelspec list`

Alternatively, details of environments are located at:
`~/.local/share/jupyter/kernels/`




## TODO
Install
sudo apt install python3.10-venv
