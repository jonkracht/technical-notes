# Logging in python

## Standard logging library

Import via `import logging`

Logger methods are named by severity.
Execute via `logger.XXX()`

--- | ---
DEBUG | Detailed information, typically of interest only when diagnosing problems 
INFO | Confirmation that things are working as expected.
WARNING | Indication that something unexpected happend, though software is still working
ERROR |  Due to a more serious problem, software has not been able to perform some function
CRITICAL | Serious error indicating program may be unable to run


Only messages above a threshold level (`loglevel`) are reported.
This level may be changed mid-program.


### Basic (root) logger setup

Configure a basic logger using `basicConfig` method:
`logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w")`

`level` sets the severity threshold at which events are recorded
`filename` specifies to output log to a file
`filemode` set to 'w' to create a new file on each run and 'a' to append logs to existing file.
`datefmt` sets format of datetime (ex.  `datefmt="%Y-%m-%d %H:%M:%S"`)



`basicConfig` can only be executed once.


#### Root logger snippet

```
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
```




### Formatting log messages

Include `format='%(levelname)s:%(message)s'` argument clause in `basicConfig` call

Available options:  https://docs.python.org/3/library/logging.html#logrecord-attributes

Some options:
* Human-readable time `%(asctime)s`
* Source line number where call was issued `%(lineno)d`


Change log-level mid-code via `logger.setLevel(logging.DEBUG)`


### Logging program variables

Use `logging.warning('%s before you %s', 'Look', 'leap!')` formatting  (i.e. %-style string formatting)

Alternatively, use f-strings:  `logging.debug(f"{some_var=}")`
Including `=` inside f-string logs both variable name and value.



### Logging exceptions

Include stack trace into log

Use `exc_info=True` argument in logging call

```
try:
    some_calc = 1 / 0
except ZeroDivisionError:
    logging.error("Calculation error", exc_info=True)
```

Alternatively: Use `logging.exception("Message here")` in except clause



### Create custom logger

Allows use of multiple loggers

Create logger:  `logger = logging.getLogger(__name__)`
'__name__' give logger the name of the module; altneratively can use any string

Create a handler:  `handler = logging.FileHandler('test.log')`

Create a formatter:  `formatter = logging.Formatter('%(asctime)s ...')`
Formatting arguments may be those as above.

Set formatter for handler:  `handler.setFormatter(formatter)`

Add the formatted handler to the logger: `logger.addHandler(handler)` 



Also StreamHandler


#### Custom logger snippet

```
logger = logging.getLogger(__name__)
handler = logging.FileHandler('log.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Here is some debug")

```



#### Dict config
Import module via `import logging.config`


Initialize via `logging.config.dictConfig(config=logging_config)`
where 'logging_config' is a dictionary of logger paramaters

Example:
```
logging_config = {
    "version" = 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext//sys.stdout",
        },
    },
    "loggers": {
        "root": {"level": "DEBUG", "handlers": ["stdout"]}
    },
}
```


Can hold this dictionary in an external json or yaml file




### Passing loglevel in from command line





## Loguru

Install package via pip.
Import via `from loguru import logger`


## References

* Real Python:  https://realpython.com/python-logging/
* https://www.youtube.com/watch?v=9L77QExPmI0
