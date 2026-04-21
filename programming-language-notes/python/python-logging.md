# Logging in python

## Standard logging library

Logger methods are named by severity:

--- | ---
DEBUG | Simply provides information 
INFO | Confirmation that things are working
WARNING | Something unexpected
ERROR | Software has not been able to perform some function
CRITICAL | Serious error, indicating program may be unable to run


Only messages above a threshold level ('loglevel') are reported.
May be configured otherwise.

Configure a basic logger using `basicConfig` function:
`logging.basicConfig(level=logging.DEBUG)`

`level` flag sets threshold at which messages are recorded.


### Export log to file
```
import logging
logger = logging.getLogger(__name__)  # names logger to program name
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

To create a new log file on each run, include `filemode='w'` in the `basicConfig` call.  Alternatively, set flag to `a` to append new entries to existing file.





### Formatting log messages
Include `format='%(levelname)s:%(message)s'` argument clause in `basicConfig` call

Available options:  https://docs.python.org/3/library/logging.html#logrecord-attributes

Some options:
* Human-readable time `%(asctime)s`
* Source line number where call was issued `%(lineno)d`


Change log-level mid-code via `logger.setLevel(logging.DEBUG)`


To include program variables in the logs, use `logging.warning('%s before you %s', 'Look', 'leap!')` formatting  (i.e. %-style string formatting)

Alternatively, use f-strings:  `logging.debug(f"{some_var=}")`
Including `=` inside f-string logs both variable name and value.



### Logging exceptions

Include `exc_info=True` in logging call

```
try:
    some_calc = 1 / 0
except ZeroDivisionError:
    logging.error("Calculation error", exc_info=True)
```

Alternatively: Use `logging.exception("Message here")` in except clause


### Passing loglevel in from command line


## Loguru


## References

* Real Python:  https://realpython.com/python-logging/
