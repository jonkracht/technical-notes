# cookiecutter

Tool for implementing standardized file structures across various software projects

Install user-created modules into current python:
`pip install -e .`


## Templates

### cookiecutter-data-science
https://cookiecutter-data-science.drivendata.org/

#### Create new ccds project
In desired directory:  `ccds`
Enter project information 


#### Set up version control
Within project directory, initialize a git repository, add all files and commit changes
`git init; git add .; git commit -m "CCDS defaults"`

Push to a shared repository


#### Setup GNU Make as a task runner

Within `Makefile`, define common project tasks (setup virtual environment, syncing data, etc.) 


#### Create a virtual envinronment

Use make commands defined in Makefile
`make create_environment`
`make requirements`


#### Add data

