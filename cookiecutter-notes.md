# cookiecutter

Tool for implementing standardized file structures across various software projects

Install user-created modules into current python:
`pip install -e .`


## Templates

### cookiecutter-data-science
https://cookiecutter-data-science.drivendata.org/


Opinions:
* Raw data is immutable so shouldn't need to be under source control
* Small amounts of data may be included in the repository (Github allows <100 MB)
* Large data sets can be stored in the cloud:  Amazon, Azure, Google

#### Create new ccds project
In desired directory:  `ccds`
Enter project information 

Select `enable_code_scaffold` to include template project files (config.py, dataset.py, features.py, plots.py)

`pyproject.toml` specifies a desired python version, something like "~=3.10.0"
Causes errors when installing packages so commenting out

#### Set up version control
Within project directory, initialize a git repository, add all files and commit changes
`git init; git add .; git commit -m "CCDS defaults"`

Push to a shared repository


#### Setup GNU Make to act as a task runner

Within `Makefile`, define commands for common project tasks:
* requirements
* create_environment
* sync_data_up

#### Create a virtual environment

Use make commands defined in Makefile
`make create_environment`
`make requirements`


#### Add data

#### Check out a branch

Helps to keep development organized especially when multiple people are contributing


#### Create a jupyter notebook

Naming convention:  
[PHASE].[NOTEBOOK_NUM]-[AUTHOR_INITIALS]-[DESCRIPTION].ipynb

where [PHASE]:
* 0:  Data exploration; exploratory work
* 1:  Data cleaning and feature creation; writes to `data/interim` or `data/processed`
* 2:  Visualizations:  writes to `reports`
* 3:  Modeling
* 4:  Publications:  notebooks that are directly turned into reports


#### Refactoring into modules

Allows code to be shared between various parts of the project (scripts, notebooks, etc.)

Enable autoreload so that most recent version is used:
```
%load_ext autoreload
%autoreload 2
```

Import functions:
from {{ cookiecutter.module_name }}.data import make_dataset
