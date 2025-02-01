## Timing a process
* Use bash time command:  `time python3 file.py`
* Use python time module:  `import time; start = time.time(); CODE HERE; end = time.time(); print(end-start)



## Parallelization

Three options:
* asyncio - good for IO bound processes
* threading - 
* multiprocessing
