## Object template

```python
# Class names use UpperCamelCase
class ObjectName(some_other_object):  # inherit from another object
    """Docstring"""

    # class attributes
    parameter_1 = "cat"
    
    # constructor initializes attributes of the instance, including default values
    def __init__(self, p1 = 0):
        self.day = "Monday"
        self.hour = p1

    # class methods
    def print_info(self):
        print(f"Today is {self.day}")

# Instantiate (i.e. create) an instance of the class
obj1 = ObjectName(13)

# Access an object's method
obj1.print_info()
```


## Timing a process
* Use bash time command:  `time python3 file.py`
* Use python time module:  `import time; start = time.time(); CODE HERE; end = time.time(); print(end-start)



## Parallelization

Three options:
* asyncio - good for IO bound processes
* threading - 
* multiprocessing
