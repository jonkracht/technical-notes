import logging

# Logging via root logger

## Configure it
logging.basicConfig(
    level=logging.DEBUG,
    filename="root-logger.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

## Example logs calls
logging.debug("Basic logging debug")
logging.info("Info")
logging.warning("Better watch out")
logging.error("Shize something went wrong")
logging.critical("Boooom")


## Log variable values
x = 2
logging.debug(f"the value of x is {x=}")


## Log exception and stack trace
try:
    y = 1 / 0
except ZeroDivisionError as e:
    logging.exception("It is a zero division error", exc_info=True)


## Create custom logger
import logging.config
